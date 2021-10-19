from bot.keyboards.inline.callbacks import callbackDatas
from emoji import *
from telebot import types

genderButtons = types.InlineKeyboardMarkup()

Men = types.InlineKeyboardButton(text=f'{MEN_EMOJI}', callback_data=callbackDatas.genderCallBack.new(
    gender="women"
))
Women = types.InlineKeyboardButton(text=f'{WOMEN_EMOJI}', callback_data=callbackDatas.genderCallBack.new(
    gender='men'
))
genderButtons.add(Men, Women)
