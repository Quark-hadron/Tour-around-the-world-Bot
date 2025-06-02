import asyncio
import os
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

from database.engine import create_db
from database.engine import drop_db

from handlers.user_privat import user_privat_router
from handlers.seasons_privat import seasons_privat_router
from handlers.people_privat import people_privat_router
from handlers.other import other_privat_router
from handlers.end_select import end_select_privat_router
from handlers.payment import payment_router
from neiro.neuro_search_router import neuro_search_router

from command.bot_cmd_list import private

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)


dp.include_router(user_privat_router)
dp.include_router(seasons_privat_router)
dp.include_router(people_privat_router)
dp.include_router(other_privat_router)
dp.include_router(end_select_privat_router)
dp.include_router(payment_router)
dp.include_router(neuro_search_router)


async def on_startup(bot):

    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown(bot):
    print('Бот упал')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)


    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

asyncio.run(main())


