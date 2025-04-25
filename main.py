#!/usr/bin/env python 
#encoding: utf-8

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
#from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio
import aiohttp
from dotenv import dotenv_values
import logging

logging.basicConfig(level=logging.INFO)
config = dotenv_values()

#Your secret telegram API token
API_TOKEN = config.get("API_TOKEN")

#Your secret Groq API token
YOUR_SECRET_GROQ_TOKEN = config.get("GROQ_TOKEN")

HOST = config.get("HOST")
PORT = config.get("PORT")
URL = f"http://{HOST}:{PORT}/"

# Set the dictionary for Groq API parametres
groq_api_params = {
    "YOUR_SECRET_GROQ_TOKEN" : YOUR_SECRET_GROQ_TOKEN,
    "MODEL": "llama-3.3-70b-versatile",
    "MESSAGES": list(),
    "TEMPERATURE": 1,
    "MAX_COMPLETION_TOKENS": 1024,
    "TOP_P": 1,
    "STREAM": False,
    "STOP": None,
}

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def response(prompt: str, url=URL) -> str:
    global groq_api_params
    groq_api_params["MESSAGES"].append({'role' : 'user', 'content' : prompt})
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=groq_api_params) as resp:
            return await resp.text()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Welcome! I'm your minimal Telegram bot")

@dp.message(F.text)
async def chat(message: Message):
    ans = await response(message.text)
    ans = ans[1:-1]
    ans = ans.replace('\\n', '\n')
    ans = ans.replace('\\"', '"')
    ans = ans.replace('\\*', '*')
    """
    ans = ans.replace('*', '\\*')
    ans = ans.replace('/', '\\/')
    ans = ans.replace('-', '\\-')
    ans = ans.replace('+', '\\+')
    ans = ans.replace('=', '\\=')
    ans = ans.replace('!', '\\!')
    ans = ans.replace('&', '\\&')
    ans = ans.replace('|', '\\|')
    ans = ans.replace('_', '\\_')
    ans = ans.replace('.', '\\.')
    ans = ans.replace('#', '\\#')
    ans = ans.replace('@', '\\@')
    ans = ans.replace('$', '\\$')
    ans = ans.replace('?', '\\?')
    ans = ans.replace('%', '\\%')
    ans = ans.replace('[', '\\[')
    ans = ans.replace(']', '\\]')
    ans = ans.replace('(', '\\(')
    ans = ans.replace(')', '\\)') 
    ans = ans.replace('{', '\\{')
    ans = ans.replace('}', '\\}') 
    ans = ans.replace('"', '\\"')
    """

    await message.answer(ans)#, parse_mode=ParseMode.MARKDOWN_V2)

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
