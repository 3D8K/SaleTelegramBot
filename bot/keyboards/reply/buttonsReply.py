from emoji import *
from telebot import types

mainMenuButtons = types.ReplyKeyboardMarkup(resize_keyboard=True)
gender = types.KeyboardButton(f'{MEN_EMOJI}/{WOMEN_EMOJI} Пол')
brand = types.KeyboardButton(f'{BRAND_EMOJI}️ Бренд')
color = types.KeyboardButton(f'{GREEN_EMOJI}Цвет')
price = types.KeyboardButton(f'{PRICE_EMOJI} Цена️')
size = types.KeyboardButton(f'{SIZE_EMOJI}Размер')
search = types.KeyboardButton(f'{SEARCH_EMOJI} Поиск')
mainMenuButtons.add(gender, brand, size, color, price, search)

