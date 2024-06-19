import asyncio
import logging

import uvicorn
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.config import settings
from api import router as api_router
from create_fastapi_app import create_app
from crud.users import set_user

main_app = create_app(create_custom_static_urls=True)

bot = Bot(token="7307113634:AAEdbmgh6_6rpOc4Qy7VrMGcm4zR2ozdtdE")
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await set_user(message.from_user.id, message.from_user.username)
    markup = (
        InlineKeyboardBuilder().button(
            text="123",
            web_app=types.WebAppInfo(url="https://www.google.com/"),
        )
    ).as_markup()
    await bot.send_message(
        message.from_user.id,
        text="123",
        reply_markup=markup,
        parse_mode="Markdown",
    )


main_app.include_router(api_router)


async def start_bot():
    logging.basicConfig(level=logging.INFO)
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error in polling: {e}")
    finally:
        await bot.session.close()


async def start_fastapi():
    config = uvicorn.Config("main:main_app", host=settings.run.host, port=settings.run.port, reload=True)
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    bot_task = asyncio.create_task(start_bot())
    api_task = asyncio.create_task(start_fastapi())
    await asyncio.gather(bot_task, api_task)

if __name__ == "__main__":
    asyncio.run(main())
