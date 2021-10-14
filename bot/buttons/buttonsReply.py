from emoji import *
from telebot import types

genderButtons = types.InlineKeyboardMarkup()
Men = types.InlineKeyboardButton(text=f'{MEN_EMOJI}', callback_data='genderMen')
Women = types.InlineKeyboardButton(text=f'{WOMEN_EMOJI}', callback_data='genderWomen')
genderButtons.add(Men, Women)
