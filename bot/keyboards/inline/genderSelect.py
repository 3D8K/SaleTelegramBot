from bot.keyboards.inline.callbacks import callbackDatas
from gui.emoji import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
genderButtons = InlineKeyboardMarkup(row_width=2)

Men = InlineKeyboardButton(text=f'{MEN_EMOJI}', callback_data=callbackDatas.genderCallBack.new(
    gender="men"
))
Women = InlineKeyboardButton(text=f'{WOMEN_EMOJI}', callback_data=callbackDatas.genderCallBack.new(
    gender='women'
))
genderButtons.add(Men, Women)
