from aiogram.filters import CommandStart, Command, or_f
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from states import TourSelection


from keyboards import reply


other_privat_router = Router()


@other_privat_router.message(F.text.lower() == 'другое кол-во людей')
async def about(message: types.Message):
    await message.answer('Введите в строку ввода кол-во людей:', reply_markup=reply.del_kd)
    await message.answer(' ', reply_markup=reply.search_kb)


@other_privat_router.message(F.text.lower() == "⬅️ назад")
async def back_from_custom_count(message: types.Message, state: FSMContext):
    await state.set_state(TourSelection.selecting_people)
    await message.answer(
        "Выберите количество людей:", 
        reply_markup=reply.people_kb
    )