import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7292194805:AAE1IWLoYpWifhdFS6XGW1elnCRKr7KjuQA")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Demo chat",
                    web_app=types.WebAppInfo(url='https://localhost:5173/'),
                )
            ]
        ]
    )
    await message.answer("Hello!", reply_markup=markup)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
