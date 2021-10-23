from gui.emoji import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

priceButtons = ReplyKeyboardMarkup(resize_keyboard=True)
priceLow = KeyboardButton(f'От  {PRICELOW_EMOJI}')
priceHigh = KeyboardButton(f'До {PRICEHIGH_EMOJI}')
Back = KeyboardButton(f'Назад {BACK_EMOJI}')
priceButtons.add(priceLow, priceHigh, Back)
