from emoji import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenuButtons = ReplyKeyboardMarkup(resize_keyboard=True)
gender = KeyboardButton(f'{MEN_EMOJI}/{WOMEN_EMOJI} Пол')
brand = KeyboardButton(f'{BRAND_EMOJI}️ Бренд')
color = KeyboardButton(f'{GREEN_EMOJI}Цвет')
price = KeyboardButton(f'{PRICE_EMOJI} Цена️')
size = KeyboardButton(f'{SIZE_EMOJI}Размер')
search = KeyboardButton(f'{SEARCH_EMOJI} Поиск')
mainMenuButtons.add(gender, brand, size, color, price, search)
