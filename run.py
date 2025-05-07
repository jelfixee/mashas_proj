import logging
import asyncio
from config import TELEGRAM_TOKEN
from aiogram import Bot, Dispatcher
from markdown_main import router

async def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())