from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

API_TOKEN = "YOUR_SECRET_TELEGRAM_TOKEN"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello! I'm minimalistic telegram Bot.")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
