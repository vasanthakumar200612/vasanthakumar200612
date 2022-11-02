from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

bot = Bot(token='5773234523:AAHJZ2rD0FlNEKQzIUL7uYH8kyFdSQH5GZ0')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="10 Below", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="100 Below", callback_data="randomvalue_of100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)


@dp.message_handler(commands=['random'])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hi, I am sample bot ")


@dp.callback_query_handler(text=["randomvalue_of10", "randomvalue_of100"])
async def random_value(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.answer(randint(1, 10))
    if call.data == "randomvalue_of100":
        await call.message.answer(randint(1, 100))
    await call.answer()


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text in ['Hi', 'hi']:
        await message.reply("Hi! How are you?")
    else:
        await message.reply(f"Your message is: {message.text}")


executor.start_polling(dp)