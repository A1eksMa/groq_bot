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

#Your secret telegram token
API_TOKEN = config.get("API_TOKEN")

HOST = config.get("HOST")
PORT = config.get("PORT")
URL = f"http://{HOST}:{PORT}/groq_single_prompt/"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def response(prompt: str, url=URL) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={"prompt": prompt}) as resp:
            return await resp.text()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Welcome! I'm your minimal Telegram bot")

@dp.message(F.text)
async def chat(message: Message):
    ans = await response(message.text)
    ans = response(message.text)
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
