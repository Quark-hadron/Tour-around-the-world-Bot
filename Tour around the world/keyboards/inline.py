from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_url_btns(
        *,
        btns: dict[str, str],
        sizes: tuple[int] = (1,),):
    
    keyboard = InlineKeyboardBuilder()

    for text, url in btns.items():

        keyboard.add(InlineKeyboardButton(text=text, callback_data=url))

    return keyboard.adjust(*sizes).as_markup()
