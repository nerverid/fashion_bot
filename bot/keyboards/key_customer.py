import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_role = KeyboardButton("Change Role")
button_styles = KeyboardButton("Styles")
button_cur_look = KeyboardButton("Current looks")

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_role)
greet_kb.add(button_styles)
greet_kb.add(button_cur_look)

style_kb = ReplyKeyboardMarkup(resize_keyboard=True)



markup = types.InlineKeyboardMarkup()
markup.add(types.InlineKeyboardButton('Site', callback_data='hello'))
markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))

