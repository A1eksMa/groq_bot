from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio
import requests
from dotenv import dotenv_values
import logging

logging.basicConfig(level=logging.INFO)
config = dotenv_values()

#Your secret telegram token
API_TOKEN = config.get("API_TOKEN")

HOST = config.get("HOST")
PORT = config.get("PORT")
URL = f"http://{HOST}:{PORT}/groq_chat/"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def response(prompt: str, url=URL):
    return requests.get(url,params={"prompt" : f"{prompt}"}).text

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello! I'm minimalistic telegram Bot.")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
