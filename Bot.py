import random,time
from aiogram import *
from aiogram.types import *

bot = Bot(token="5114052117:AAH2ZINSWNf-9YSP8p3Bzh-Mk3gKEMppbq4")
dp = Dispatcher(bot)

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

@dp.message_handler(commands=['tiktok'])
async def tiktok(message: types.Message):
    
    tikaccount = InlineKeyboardButton('Тик ток админа:',url='youtube.com')
    tikinline = InlineKeyboardMarkup().add(tikaccount)
    await message.answer("тик ток внизу:",reply_markup=tikinline)

@dp.message_handler(content_types=["started_a_new_video_chat"])
async def video_chat(message: types.Message):
    await message.answer("sdfdssdgfgdfg")

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)