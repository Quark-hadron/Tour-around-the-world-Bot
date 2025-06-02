from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types


from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_keyboard(buttons: list[str], sizes: tuple[int] = (2,)):
    builder = ReplyKeyboardBuilder()
    for button in buttons:
        builder.button(text=button)
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)

# Кнопки для поиска
search_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔍 Поиск туров"), KeyboardButton(text="🧠 Поиск туров с нейро")],
        [KeyboardButton(text="💳 Варианты оплаты"), KeyboardButton(text="📍 Где нас найти")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
)


back_btn = KeyboardButton(text="⬅️ Назад")

# Обновляем клавиатуры с добавлением кнопки "Назад"
people_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"), KeyboardButton(text="2")],
        [KeyboardButton(text="3"), KeyboardButton(text="4")],
        [KeyboardButton(text="Другое кол-во людей")],
        [back_btn]  # Добавляем кнопку назад
    ],
    resize_keyboard=True
)

seasons_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Зима"), KeyboardButton(text="Осень")],
        [KeyboardButton(text="Лето"), KeyboardButton(text="Весна")],
        [back_btn]  # Добавляем кнопку назад
    ],
    resize_keyboard=True
)

type_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Горнолыжный"), KeyboardButton(text="Пляжный")],
        [KeyboardButton(text="Экскурсионный")],
        [back_btn]  # Добавляем кнопку назад
    ],
    resize_keyboard=True
)

# Клавиатура для этапа ввода количества людей вручную
back_only_kb = ReplyKeyboardMarkup(
    keyboard=[[back_btn]],
    resize_keyboard=True
)

# Клавиатура для удаления
del_kd = ReplyKeyboardRemove()

