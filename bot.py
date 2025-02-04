import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN, OWNER_ID

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.from_user.id == OWNER_ID:
        await message.answer("Ты - владелец! Можешь майнить бесплатно!")
    else:
        await message.answer("Привет! Для начала майнинга тебе нужно будет потратить Telegram Stars или Toncoin.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
