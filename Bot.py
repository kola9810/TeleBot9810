import random,time
from aiogram import *
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


bot = Bot(token="5114052117:AAH2ZINSWNf-9YSP8p3Bzh-Mk3gKEMppbq4")
dp = Dispatcher(bot)

@dp.message_handler(text=['.','.'])
async def messages(message: types.Message):
    await message.delete()

@dp.message_handler(content_types=["new_chat_members"])
async def newUser(message: types.Message):
    print('someone connect')

    welcome = random.randint(1,6)

    if welcome == 1:
        
        await message.answer("Добро пожаловать в роблкс хавуc")
        
    if welcome == 2:
        await message.answer("Привет (●'◡'●) \nмне 10 лет\nя Коля\nнадеюсь в этом хавусе вам будет комфортно:3❤️")
        
        
    if welcome == 3:
        await message.answer("Прив (●'\nмне 10 лет\nя Коля\nнадеюсь мы подружимся◡'●)")
        

    if welcome == 4:
        await message.answer("Пр (●'◡'●) \nя Коля\nмне 10 лет\nи наслаждайтесь чатом❤️")
        
        
    if welcome == 5:
        await message.answer("Приветики\nя Коля\nмне 10 лет\nнадеюсь в этом хавусе вам будет комфортно:)❤️❤️")
        


playmark = ReplyKeyboardMarkup(resize_keyboard=True)
abobtmi = KeyboardButton("в AdoptMe")
mm2 = KeyboardButton('Murder mustory2')
ikea = KeyboardButton('В икею')

exitpl = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1).add(KeyboardButton('.'))

playmark.add(abobtmi,mm2,ikea)

@dp.message_handler(commands=['play','играть','play@MikolaCatBot'])
async def play(message: types.Message):
    await message.answer('во что поиграть',reply_markup=playmark)
    
@dp.message_handler(text=['В икею','Murder mustory2','в AdoptMe'])
async def exit(message: types.Message):
    await message.answer(".",reply_markup=exitpl)
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)