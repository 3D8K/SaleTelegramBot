from bot.keyboards.inline.callbacks import callbackDatas
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

brandButtons = InlineKeyboardMarkup()
Adidas = InlineKeyboardButton(text='Adidas', callback_data=callbackDatas.brandCallBack.new(brand="adidas"))
Nike = InlineKeyboardButton(text='Nike', callback_data=callbackDatas.brandCallBack.new(brand='Nike'))
NewBalance = InlineKeyboardButton(text='New Balance',
                                  callback_data=callbackDatas.brandCallBack.new(brand='New Balance'))
Converse = InlineKeyboardButton(text='Converse', callback_data=callbackDatas.brandCallBack.new(brand='Converse'))
Puma = InlineKeyboardButton(text='Puma', callback_data=callbackDatas.brandCallBack.new(brand='Puma'))
Reebok = InlineKeyboardButton(text='Reebok', callback_data=callbackDatas.brandCallBack.new(brand='Reebook'))
DrMartens = InlineKeyboardButton(text='Dr Martens', callback_data=callbackDatas.brandCallBack.new(brand='Dr Martens'))
FredPerry = InlineKeyboardButton(text='Fred Perry', callback_data=callbackDatas.brandCallBack.new(brand='FredPerry'))
Asics = InlineKeyboardButton(text='Asics', callback_data=callbackDatas.brandCallBack.new(brand='Asics'))
Vans = InlineKeyboardButton(text='Vans', callback_data=callbackDatas.brandCallBack.new(brand='Vans'))
brandButtons.add(Adidas, Asics, DrMartens, Reebok, Puma, Nike, NewBalance, Converse, Vans, FredPerry)
