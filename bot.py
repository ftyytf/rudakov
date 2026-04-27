import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.INFO)

load_dotenv()  # загрузить .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Ошибка: BOT_TOKEN не найден в .env")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Бот запущен и готов к работе.")

async def main():
    try:
        logging.info("Запуск бота...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
