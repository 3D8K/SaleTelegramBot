from bot.keyboards.inline.callbacks import callbackDatas
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

sizeButtons = InlineKeyboardMarkup()
size365 = InlineKeyboardButton(text='36.5', callback_data=callbackDatas.sizeCallBack.new(size='36.5'))
size37 = InlineKeyboardButton(text='37', callback_data=callbackDatas.sizeCallBack.new(size='37'))
size375 = InlineKeyboardButton(text='37.5', callback_data=callbackDatas.sizeCallBack.new(size='37.5'))
size38 = InlineKeyboardButton(text='38', callback_data=callbackDatas.sizeCallBack.new(size='38'))
size385 = InlineKeyboardButton(text='38.5', callback_data=callbackDatas.sizeCallBack.new(size='38.5'))
size39 = InlineKeyboardButton(text='39', callback_data=callbackDatas.sizeCallBack.new(size='39'))
size395 = InlineKeyboardButton(text='39.5', callback_data=callbackDatas.sizeCallBack.new(size='39.5'))
size40 = InlineKeyboardButton(text='40', callback_data=callbackDatas.sizeCallBack.new(size='40'))
size405 = InlineKeyboardButton(text='40.5', callback_data=callbackDatas.sizeCallBack.new(size='40.5'))
size41 = InlineKeyboardButton(text='41', callback_data=callbackDatas.sizeCallBack.new(size='41'))
size415 = InlineKeyboardButton(text='41.5', callback_data=callbackDatas.sizeCallBack.new(size='41.5'))
size42 = InlineKeyboardButton(text='42', callback_data=callbackDatas.sizeCallBack.new(size='42'))
size425 = InlineKeyboardButton(text='42.5', callback_data=callbackDatas.sizeCallBack.new(size='42.5'))
size43 = InlineKeyboardButton(text='43', callback_data=callbackDatas.sizeCallBack.new(size='43'))
size435 = InlineKeyboardButton(text='43.5', callback_data=callbackDatas.sizeCallBack.new(size='43.5'))
size44 = InlineKeyboardButton(text='44', callback_data=callbackDatas.sizeCallBack.new(size='44'))
size445 = InlineKeyboardButton(text='44.5', callback_data=callbackDatas.sizeCallBack.new(size='44.5'))
size45 = InlineKeyboardButton(text='45', callback_data=callbackDatas.sizeCallBack.new(size='45'))
size455 = InlineKeyboardButton(text='45.5', callback_data=callbackDatas.sizeCallBack.new(size='45.5'))
size46 = InlineKeyboardButton(text='46', callback_data=callbackDatas.sizeCallBack.new(size='46'))
size465 = InlineKeyboardButton(text='46.5', callback_data=callbackDatas.sizeCallBack.new(size='46.5'))
sizeButtons.add(size365, size37, size375, size38, size385, size39, size395, size40, size405, size41, size415, size42,
                size425, size43, size435,
                size44, size445, size45, size455, size46, size465)
