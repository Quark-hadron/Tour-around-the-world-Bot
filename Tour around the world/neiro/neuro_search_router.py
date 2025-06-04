from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from keyboards import reply
from states import TourSelection, UserWishState
from neiro.neural_search import find_similar_tours
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.models import Tour, UserWish
from database.engine import session_maker

neuro_search_router = Router()


@neuro_search_router.callback_query(F.data.startswith('search_neiro'))
async def start_neuro_search(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(TourSelection.neuro_search)
    await callback.message.answer(
        "Опишите ваш идеальный тур:\n\nПримеры:\n"
        "- Пляжный отдых в теплой стране\n"
        "- Горнолыжный курорт с детьми\n"
        "- Экскурсии по историческим местам",
        reply_markup=types.ReplyKeyboardRemove()
    )
    


@neuro_search_router.message(TourSelection.neuro_search)
async def process_neuro_search(message: types.Message, state: FSMContext):
    user_query = message.text

    wish_text = message.text.strip()
    await state.set_state(UserWishState.waiting_for_wish)


    user_id = message.from_user.id
    
    async with session_maker() as session:
        new_wish = UserWish(
            user_id=user_id,
            wish_text=wish_text
        )
        session.add(new_wish)
        await session.commit()
        await session.close()


    await message.answer("🔎 Ищу лучшие варианты...")
    
    try:
        tours = await find_similar_tours(user_query)
        
        if not tours:
            await message.answer("😔 Ничего не найдено. Попробуйте изменить запрос.", reply_markup=reply.keyboard_back)
            return
            
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
                f"🌟 <b>Нейропоиск нашел:</b>\n\n"
                f"🌍 {tour.country}, {tour.city}\n"
                f"📅 {tour.in_date.strftime('%d.%m.%Y')}-{tour.out_date.strftime('%d.%m.%Y')}\n"
                f"👥 Для {tour.count_people} чел. | {smile} {tour.seasons}\n"
                f"🏷 Тип: {tour.tour_type}\n"
                f"✨ Рейтинг: {tour.rating}\t{rating_smile}\n"
                f"💵 Цена: {tour.price:.2f} руб.\n"
                f"📝 {tour.description}"
            )
            
            buy_button = InlineKeyboardButton(
                text="💳 Купить",
                callback_data=f"buy_{tour.id}"
            )
            keyboard = InlineKeyboardMarkup(inline_keyboard=[[buy_button]])
            
            if tour.image:
                await message.answer_photo(tour.image, caption=tour_info, reply_markup=keyboard)
            else:
                await message.answer(tour_info, reply_markup=keyboard)

        await message.answer('Если не подшли предложения от нейро. Tы можешь вернуться на главную и найти что-то другое', reply_markup=reply.keyboard_back)
                
    except Exception as e:
        await message.answer(f"⚠️ Ошибка: {str(e)}",reply_markup=reply.keyboard_back)
    finally:
        await state.clear()