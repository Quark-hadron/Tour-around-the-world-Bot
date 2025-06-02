from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.models import Tour
from database.engine import session_maker
from database.orm_query import orm_get_tour

payment_router = Router()

@payment_router.callback_query(F.data.startswith("buy_"))
async def buy_tour(callback: types.CallbackQuery, state: FSMContext):
    
    try:
        # Извлекаем ID тура из callback_data
        tour_id = int(callback.data.split("_")[1])
        
        # Получаем информацию о туре из БД
        async with session_maker() as session:
            tour = await orm_get_tour(session, tour_id)
            
        if not tour:
            await callback.message.answer("❌ Тур не найден")
            await callback.answer()
            return
        
        # Сохраняем информацию о выбранном туре в состоянии
        await state.update_data(
            tour_id=tour.id,
            tour_price=tour.price,
            tour_title=f"{tour.country}, {tour.city}"
        )
        
        # Создаем клавиатуру для оплаты
        payment_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💳 Оплатить", callback_data="confirm_payment")],
            [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_payment")]
        ])
        
        # Отправляем сообщение с формой оплаты
        await callback.message.answer(
            f"💳 <b>Оформление заказа</b>\n\n"
            f"🏙 Тур: {tour.country}, {tour.city}\n"
            f"📅 Период: {tour.in_date.strftime('%d.%m.%Y')}-{tour.out_date.strftime('%d.%m.%Y')}\n"
            f"💵 Сумма к оплате: <b>{tour.price:.2f} руб.</b>\n\n"
            "Нажмите 'Оплатить' для завершения покупки",
            reply_markup=payment_keyboard
        )
        
        await callback.answer()
        
    except Exception as e:
        await callback.message.answer(f"⚠️ Ошибка: {str(e)}")
        await callback.answer()

@payment_router.callback_query(F.data == "confirm_payment")
async def confirm_payment(callback: types.CallbackQuery, state: FSMContext):
    try:
        # Получаем данные о туре из состояния
        data = await state.get_data()
        tour_id = data.get("tour_id")
        price = data.get("tour_price")
        title = data.get("tour_title")
        
        # Здесь должна быть интеграция с платежной системой
        # Для примера просто эмулируем успешную оплату
        
        # Отправляем сообщение об успешной оплате
        await callback.message.answer(
            "✅ <b>Оплата прошла успешно!</b>\n\n"
            f"🏙 Тур: {title}\n"
            f"💵 Сумма: {price:.2f} руб.\n\n"
            "В ближайшее время с вами свяжется наш менеджер для уточнения деталей."
        )
        
        # Отправляем уведомление администратору
        # (в реальном боте здесь должна быть реализация отправки уведомления)
        
        await callback.answer("Оплата прошла успешно!")
        await state.clear()
        
    except Exception as e:
        await callback.message.answer(f"⚠️ Ошибка при обработке платежа: {str(e)}")
        await callback.answer()

@payment_router.callback_query(F.data == "cancel_payment")
async def cancel_payment(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("❌ Оплата отменена")
    await callback.message.answer('Зайдите в меню и вернитесь к началу поиска')
    await state.clear()
    await callback.answer()
