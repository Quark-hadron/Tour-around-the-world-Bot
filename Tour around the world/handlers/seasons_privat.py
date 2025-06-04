from aiogram.filters import CommandStart, Command, or_f
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from database.models import Tour, Tour_user
from keyboards.inline import get_url_btns
from states import TourSelection
from database.orm_query import orm_get_tours
from database.engine import session_maker
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from keyboards import reply


seasons_privat_router = Router()


@seasons_privat_router.message(TourSelection.selecting_season, F.text.lower() == "⬅️ назад")
async def back_from_season(message: types.Message, state: FSMContext):
    await state.set_state(TourSelection.selecting_people)
    await message.answer(
        "Выберите количество людей:", 
        reply_markup=reply.people_kb
    )

@seasons_privat_router.message(TourSelection.selecting_tour_type, F.text.lower() == "⬅️ назад")
async def back_from_tour_type(message: types.Message, state: FSMContext):
    await state.set_state(TourSelection.selecting_season)
    await message.answer(
        "Выберите сезон:", 
        reply_markup=reply.seasons_kb
    )


@seasons_privat_router.message(TourSelection.selecting_season, F.text.capitalize().in_(["Зима", "Осень", "Лето",'Весна']))
async def tour_seasons_selected(message: types.Message, state: FSMContext):
    await state.update_data(season=message.text.capitalize())
    await state.set_state(TourSelection.selecting_season)
    await message.answer("Выберите тип отдыха:", reply_markup=reply.type_kb)


@seasons_privat_router.message(TourSelection.selecting_season, F.text.capitalize().in_(["Горнолыжный", "Пляжный", "Экскурсионный"]))
async def tour_type_selected(message: types.Message, state: FSMContext):
    await state.update_data(tour_type=message.text.capitalize())

    await state.set_state(TourSelection.selecting_tour_type)
    await message.answer("Вот несколько туров по вашим запросам", reply_markup=reply.del_kd)
    


    try:
        # Получаем все сохраненные данные из состояния
        data = await state.get_data()
        
        # Проверяем наличие необходимых данных
        count_people = data.get("count_people")
        season = data.get("season")
        tour = data.get('type_tour')
        
        if not count_people or not season:
            await message.answer("❌ Не удалось получить данные поиска. Пожалуйста, начните заново.", reply_markup=reply.keyboard_back)
            await state.clear()
            return
        
        tour_type = message.text.capitalize()
        
        # Сохраняем тип тура в состоянии
        await state.update_data(tour_type=tour_type)
        
        # Ищем туры в БД
        from database.orm_query import orm_get_tours  # Локальный импорт
        from database.engine import session_maker
        
        async with session_maker() as session:
            tours = await orm_get_tours(
                session=session,
                count_people=count_people,
                season=season,
                tour_type=tour_type
            )
        
        # Отправляем результаты
        if tours:
            for tour in tours:
                if tour.seasons == 'Зима':
                    smile = '🌨️'
                elif tour.seasons == 'Осень':
                    smile = '🌧️'

                elif tour.seasons == 'Лето':
                    smile = '☀️'
                else:
                    smile = '⛅'


                rating = round(tour.rating)

                if rating >=0 and rating <=1:
                    rating_smile = '⭐☆☆☆☆'
                elif rating >=1 and rating <=2:
                    rating_smile = '⭐⭐☆☆☆'
                elif rating >=2 and rating <=3:
                    rating_smile = '⭐⭐⭐☆☆'
                elif rating >=3 and rating <=4:
                    rating_smile = '⭐⭐⭐⭐☆'
                elif rating >=4 and rating <=5:
                    rating_smile = '⭐⭐⭐⭐⭐'


                tour_info = (
                    f"🌍 {tour.country}, {tour.city}\n"
                    f"📅 {tour.in_date.strftime('%d.%m.%Y')}-{tour.out_date.strftime('%d.%m.%Y')}\n"
                    f"👥 Для {tour.count_people} чел. | {smile} {tour.seasons}\n"
                    f"🏷 Тип: {tour.tour_type}\n"
                    f"✨ Рейтинг: {tour.rating}\t{rating_smile}\n"
                    f"💵 Цена: {tour.price:.2f} руб.\n"
                    f"📝 {tour.description}"
                )

                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text="💳 Купить", callback_data=f"buy_{tour.id}")],
                        [InlineKeyboardButton(text='⬅️ На главную', callback_data='back_menu_btn')],])

                if tour.image:
                    await message.answer_photo(tour.image, caption=tour_info, reply_markup=keyboard)
                else:
                    await message.answer(tour_info, reply_markup=keyboard)
        else:
            await message.answer("😔 К сожалению, по вашим критериям туров не найдено", reply_markup=reply.keyboard_back)
    
    except Exception as e:
        await message.answer(f"⚠️ Произошла ошибка: {str(e)}",reply_markup=reply.keyboard_back)
        print(f"Ошибка при поиске туров: {e}", reply_markup=reply.keyboard_back)
    
    finally:
        await state.clear()