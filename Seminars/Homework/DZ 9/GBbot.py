import telebot
#token='5671094069:AAE8MGojJf9ScZm_tP8bJMpp5BbtkbwN47E'

import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5671094069:AAE8MGojJf9ScZm_tP8bJMpp5BbtkbwN47E")
# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "main":
    asyncio.run(main())
