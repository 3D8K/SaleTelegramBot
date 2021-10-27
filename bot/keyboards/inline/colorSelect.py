from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.keyboards.inline.callbacks import callbackDatas
from gui.emoji import *

colorsButton = InlineKeyboardMarkup()
white = InlineKeyboardButton(text=f'{WHITE_EMOJI}', callback_data= callbackDatas.colorCallBack.new(color='white'))
black = InlineKeyboardButton(text=f'{BLACK_EMOJI}', callback_data= callbackDatas.colorCallBack.new(color='black'))
brown = InlineKeyboardButton(text=f'{BROWN_EMOJI}', callback_data=callbackDatas.colorCallBack.new(color='brown'))
red = InlineKeyboardButton(text=f'{RED_EMOJI}', callback_data=callbackDatas.colorCallBack.new(color='red'))
orange = InlineKeyboardButton(text=f'{ORANGE_EMOJI}', callback_data=callbackDatas.colorCallBack.new(color='orange'))
yellow = InlineKeyboardButton(text=f'{YELLOW_EMOJI}', callback_data=callbackDatas.colorCallBack.new(color='yellow'))
purple = InlineKeyboardButton(text=f'{PURPLE_EMOJI}', callback_data=callbackDatas.colorCallBack.new(color='purple'))
blue = InlineKeyboardButton(text=f'{BLUE_EMOJI}', callback_data=callbackDatas.colorCallBack.new(color='blue'))
green = InlineKeyboardButton(text=f'{GREEN_EMOJI}', callback_data=callbackDatas.colorCallBack.new(color='green'))
noneColor = InlineKeyboardButton(text='Любой цвет', callback_data=callbackDatas.colorCallBack.new(color='any'))
colorsButton.add(white, black, brown, green, blue, purple, yellow, orange, red, noneColor)