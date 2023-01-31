from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import  os



bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)

'''**********************************************КЛИЕНТСКАЯ ЧАСТЬ****************'''
@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/MyFreePracticeBot')

@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.frpm_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная, 15')

@dp.message_handler(commands=['Меню'])



'''**********************************************АДМИНСКАЯ ЧАСТЬ*****************'''

'''**********************************************ОБЩАЯ ЧАСТЬ*********************'''

@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == "Привет":
        await message.answer("И тебе привет")
    
    #await message.reply(message.text)
    #await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True)