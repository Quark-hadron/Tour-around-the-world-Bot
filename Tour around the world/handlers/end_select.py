from aiogram.filters import CommandStart, Command, or_f
from aiogram import types, Router, F
from database.models import Base

from keyboards import reply
from aiogram.fsm.context import FSMContext
from states import TourSelection


end_select_privat_router = Router()



@end_select_privat_router.message(F.text.lower() == '⬅️ назад')
async def cancel_search(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Поиск отменен. Чтобы начать заново, нажмите 'Поиск туров'.",
        reply_markup=reply.search_kb
    )


@end_select_privat_router.message(F.text.lower() == '🔍 поиск туров')
async def start_search(message: types.Message, state: FSMContext):
    await state.set_state(TourSelection.selecting_people)
    await message.answer(
        "Выберите количество людей:",
        reply_markup=reply.people_kb
    )
