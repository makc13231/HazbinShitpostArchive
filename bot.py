import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Логирование — мастхэв для хостинга
logging.basicConfig(level=logging.INFO)

async def start_handler(message: Message):
    await message.reply("Привет! Я асинхронный бот.")

async def main():
    bot = Bot(token="5402718922:AAH9rd6ZQKn0OzkviuRirEBO1wnPuUyIPeY")
    dp = Dispatcher()
    
    dp.message.register(start_handler, Command("start"))
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())