# from aiogram import types, KeyboardButton
from loader import dp
from keyboards import commands_default_keyboard
from aiogram import types

# @dp.message_handler(commands='start')
# async def answer_start_command():
#     commands_default_keyboard
#     # await message.answer('Чтобы начвть работу, откройте клавиатуру в нижнем углу экрана')
    
    
@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    keyboard = commands_default_keyboard
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # buttons = ["Правила чата", "Разместить свое объявление"]
    # buttons2 = ["Заказать рекламу", "Условия рекламы"]
    # keyboard.add(*buttons)
    # keyboard.add(*buttons2)
    await message.answer("Что Вас интересует?", reply_markup=keyboard)
    # await message.reply(f'Если передумаете, напишите "отмена"')
    
# @dp.message_handler(commands='')
# async def cmd_add_photo(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button = ["+", "-"]
#     keyboard.add(*button)