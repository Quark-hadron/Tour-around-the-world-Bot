from aiogram.filters import CommandStart, Command, or_f
from aiogram import types, Router, F
from requests import session
from aiogram.fsm.context import FSMContext

from keyboards import reply
from states import TourSelection

people_privat_router = Router()


@people_privat_router.message(TourSelection.selecting_people, F.text.lower() == "⬅️ назад")
async def back_from_people(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Поиск отменен. Чтобы начать заново, нажмите 'Поиск туров'.",
        reply_markup=reply.search_kb
    )


@people_privat_router.message(F.text.lower().in_(["1", "2", "3", "4"]))
async def people_count_selected(message: types.Message, state: FSMContext):
    # Конвертируем текстовый выбор в число
    choice = message.text.lower()
    count_map = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
    }
    
    await state.update_data(count_people=count_map[choice])
    await state.set_state(TourSelection.selecting_season)
    await message.answer("Выберите сезон:", reply_markup=reply.seasons_kb)

@people_privat_router.message(TourSelection.selecting_people, F.text.isdigit())
async def custom_people_count(message: types.Message, state: FSMContext):
    try:
        count = int(message.text)
        if count < 1:
            await message.answer("Число должно быть больше 0!")
            return
            
        await state.update_data(count_people=count)
        await state.set_state(TourSelection.selecting_season)
        await message.answer("Выберите сезон:", reply_markup=reply.seasons_kb)
    except ValueError:
        await message.answer("Пожалуйста, введите число!")