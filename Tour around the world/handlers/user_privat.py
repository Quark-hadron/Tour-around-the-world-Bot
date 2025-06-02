from aiogram.filters import CommandStart, Command, or_f
from aiogram import types, Router, F
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from keyboards import reply

user_privat_router = Router()


# Приветсвие + описание бота
@user_privat_router.message(CommandStart())
async def start(message: types.Message):
       await message.answer(
        "Забудь про часы поиска! Наш бот – твой личный турагент-гений. "
        "Нажми '🔍 Поиск туров' ➡️ Выбери кол-во одыхающих ➡️ выбери Сезон ➡️ Выбери тип отдыха ➡️ Получи ТОП-подборку туров!"
        "Пляжи, горы, города или экстрим? У нас найдется идеальная поездка именно для тебя. Жми и начни свое приключение!" \
        " А если не знаешь куда хочешь?" \
        " Раскажи свои желания нашему нейросотруднику. И он подберет для тебя лучшие туры в соответствии с твоими желаниями. Удачи!😉",
        reply_markup=reply.search_kb
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
@user_privat_router.message((F.text.lower().contains('оплат')) | (F.text.lower() == 'Варианты оплаты'))
@user_privat_router.message(Command('payment'))
async def payment(message: types.Message):

    text = as_marked_section(
        Bold('Варианты оплаты:'),
        'Картой в боте',
        'На месте карта/кеш',
        'В оффисе',
        marker='✅ '
    )
    await message.answer(text.as_html())

@user_privat_router.message((F.text.lower().contains('нас найти')) | (F.text.lower() == 'Где нас можно найти:'))
@user_privat_router.message(Command('where'))
async def about(message: types.Message):

    text = as_marked_section(
        Bold('Где нас можно найти:'),
        'VK',
        'Telegram',
        'Instagram',
        'FaceBook',
        marker='♦️ '
    )
    await message.answer(text.as_html())
