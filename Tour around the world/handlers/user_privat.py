from aiogram.filters import CommandStart, Command, or_f
from aiogram import types, Router, F
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from aiogram.fsm.context import FSMContext

from keyboards import reply

user_privat_router = Router()


# Приветсвие + описание бота
@user_privat_router.message(F.text.lower() == '⬅️ на главную')
@user_privat_router.message(CommandStart())
async def start(message: types.Message):
       await message.answer('Привет!',reply_markup=reply.del_kd)
       await message.answer(
        "Забудь про ⌚ часы поиска!\nНаш бот – твой личный турагент-гений. \n\n"
        "\t➡️ Нажми: 🔍 Поиск туров\n\t➡️ Выбери кол-во одыхающих\n\t➡️ выбери Сезон\n\t➡️ Выбери тип отдыха\n\t➡️ Получи ТОП-подборку туров!\n\n"
        "Пляжи, горы, города или экстрим?\nУ нас найдется идеальная поездка именно для тебя.\nЖми и начни свое приключение!\n\n" \
        "А если не знаешь куда хочешь?\n" \
        "Раскажи свои желания нашему нейро-сотруднику.\nИ он подберет для тебя лучшие туры в соответствии с твоими желаниями.\n\n\t\tУдачи!😉",
        reply_markup=reply.markup_search
    )


@user_privat_router.callback_query(F.data.startswith('back_menu_btn'))
async def new_start(callback: types.CallbackQuery):
       await callback.message.answer('Привет!',reply_markup=reply.del_kd)
       await callback.message.answer(
        "Забудь про ⌚ часы поиска!\nНаш бот – твой личный турагент-гений. \n\n"
        "\t➡️ Нажми: 🔍 Поиск туров\n\t➡️ Выбери кол-во одыхающих\n\t➡️ выбери Сезон\n\t➡️ Выбери тип отдыха\n\t➡️ Получи ТОП-подборку туров!\n\n"
        "Пляжи, горы, города или экстрим?\nУ нас найдется идеальная поездка именно для тебя.\nЖми и начни свое приключение!\n\n" \
        "А если не знаешь куда хочешь?\n" \
        "Раскажи свои желания нашему нейро-сотруднику.\nИ он подберет для тебя лучшие туры в соответствии с твоими желаниями.\n\n\t\tУдачи!😉",
        reply_markup=reply.markup_search
    )
       
       
# О нас
@user_privat_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('Бренд "N" представлен на рынке с 1995 года.' 
    ' Сегодня оператор занимает лидирующие позиции в туристической отрасли и позиционируется как марка надежности и качества.' 
    ' Клиентов "N" в Турции, Египте, Греции, Испании, ОАЭ, Таиланде и Вьетнаме обслуживают принимающая компания Odeon Tours.' 
    ' Туроператор "N" предлагает лучшие курорты и отели в 40 странах мира, среди которых Австрия, Андорра, Бахрейн, Беларусь,' 
    ' Болгария, Вьетнам, Греция, Грузия, Доминиканская Республика, Египет, Израиль, Индия, Индонезия, Иордания, Испания,' 
    ' Италия, Катар, Кения, Кипр, Куба, Маврикий, Мальдивы, Марокко, Мексика, ОАЭ, Россия, Сейшелы, Сингапур, Таиланд,' 
    ' Танзания, Тунис, Турция, Узбекистан, Хорватия, Черногория, Шри-Ланка. Идет постоянная работа по открытию новых направлений.' 
    ' Туроператор организует групповые и индивидуальные туры FIT на базе собственных чартерных программ и регулярных рейсов, занимается развитием инсентив-,' 
    ' конгресс-, спортивного и других видов туризма, а также активно продает авиабилеты в онлайн.'
    '\n'
    '\n'
    ' Приятного поиска. Спасибо!😉')

# Оплата
@user_privat_router.callback_query(F.data.startswith('payment_tour'))
async def payment(callback: types.CallbackQuery):

    text = as_marked_section(
        Bold('Варианты оплаты:'),
        'Картой в боте',
        'На месте карта/кеш',
        'В оффисе',
        marker='✅ '
    )
    await callback.message.answer(text.as_html())

@user_privat_router.callback_query(F.data.startswith('where_tour'))
async def about(callback: types.CallbackQuery):

    text = as_marked_section(
        Bold('Где нас можно найти:'),
        'VK',
        'Telegram',
        'Instagram',
        'FaceBook',
        marker='♦️ '
    )
    await callback.message.answer(text.as_html())