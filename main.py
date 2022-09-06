import asyncio
from aiogram import Bot, Dispatcher, executor, types




bot = Bot(token="5794907150:AAEH4NGoOhx15nvYNnWUZyIZobwIDCwfhXs")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im URL Uploader bot! Send URL!")

@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == 'Hi':
        await message.reply("Hi! How are you?")
    else:
        await message.answer_video(f'{message.text}')



if __name__ == '__main__':
    executor.start_polling(dp)
