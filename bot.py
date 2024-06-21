from aiogram import *
from aiogram.filters.command import Command
from aiogram.types import WebAppInfo
import asyncio

bot = Bot(token="5679284874:AAFrLw2exw3en1zWJYLQI1MTben7Bsx0JWk")
# Диспетчер
dp = Dispatcher()


web_app = WebAppInfo(url='site_url')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Site', web_app=web_app)]
    ],
    resize_keyboard=True
)

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
        await bot.send_message(message.chat.id, 'Тестируем WebApp!', reply_markup=keyboard)
    

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())