from aiogram import Bot, types, Dispatcher, executor
from aiogram.types.web_app_info import WebAppInfo


bot = Bot(token='1945345757:AAHvxmD31AKVm3okGCzW-dW0ctAZe8DUIKg')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть веб', web_app=WebAppInfo(url='https://500kilogram.github.io/Ton-quiz/')))
    await message.answer('Привет', reply_markup=markup)


executor.start_polling(dp)