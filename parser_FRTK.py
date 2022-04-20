# Импорт нужных нам библиотек
import asyncio
import os
import random
import uuid
 
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InputFile, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
 
TOKEN = "5038773990:AAEbnLxjJkzkyYjdPnV7grm3drvJaR0x2J8"
 
bot = Bot(token=TOKEN)
 
storage = MemoryStorage()
 
dp = Dispatcher(bot, storage=storage)
 
@dp.message_handler(CommandStart())
async def start(message: types.Message):
 
    await message.answer("Приветствую пользователь, я бот дедлайнов",
                         reply_markup=ReplyKeyboardMarkup(
                             [
                                 [
                                     KeyboardButton(text="Текущие дедлайны"),
                                     KeyboardButton(text="Просроченные дедлайны ")
                                 ],
                                 [
                                     KeyboardButton(text="Получить мотивацию")
                                 ]
                             ],
                             resize_keyboard=True
                         ))
 
 
@dp.message_handler(text="Получить мотивацию")
async def notify(message: types.Message):
    text = random.choice([x for x in os.listdir("motivation/text")
                          if os.path.isfile(os.path.join("motivation/text", x))])
    text = open(f"motivation/text/{text}", "r", encoding="utf-8")
    await message.answer(text=text.read())
    text.close()
 
 
 
    @dp.message_handler(text="Просроченные дедлайны")
    async def start(message: types.Message, state: FSMContext):
        await message.answer("Список просроченных дедлайнов:",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="Назад", callback_data="back")
                                     ]
                                 ]
                             ))
 
 
@dp.message_handler(text="Текущие дедлайны")
async def start(message: types.Message, state: FSMContext):
 
    await message.answer("Список дедлайнов текущих:",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="Назад", callback_data="back")
                                 ]
                             ]
                         ))
 
 
# Создаём функцию отлавливающую кнопку назад для отмены действия
@dp.callback_query_handler(text="back", state="*")
async def get_back(call: types.CallbackQuery, state: FSMContext):
 
    # Отвечаем на нажатие кнопки, чтобы кнопка не ждала ответа и не выдавала ошибку
    await call.answer(cache_time=10)
 
    await call.message.answer("Вы вернулись",
                              reply_markup=ReplyKeyboardMarkup(
                                  [
                                      [
                                          KeyboardButton(text="Текущие дедлайны"),
                                          KeyboardButton(text="Просроченные дедлайны")
                                      ]
                                  ],
                                  resize_keyboard=True
                              ))
 
    await call.message.delete()
 
    await state.finish()
 
if __name__ == '__main__':
    from aiogram import executor
    loop = asyncio.get_event_loop()
 
    executor.start_polling(dp)