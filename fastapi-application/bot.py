import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7307113634:AAEdbmgh6_6rpOc4Qy7VrMGcm4zR2ozdtdE")
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    markup = (
        InlineKeyboardBuilder().button(
            text="login",
            web_app=types.WebAppInfo(url="https://tg-clicker.netlify.app/"),
        )
    ).as_markup()
    await message.answer("Click to login", reply_markup=markup)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
