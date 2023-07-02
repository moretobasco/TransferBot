import asyncio

from aiogram import Bot, Dispatcher
from config_data.config_bot import BotConfig, load_bot_config
import asyncpg
from config_data.config_db import DBConfig, load_db_config
from db.db_work import create_table
from handlers import test_handler


async def main():

    bot_config: BotConfig = load_bot_config()
    bot: Bot = Bot(token=bot_config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(test_handler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())