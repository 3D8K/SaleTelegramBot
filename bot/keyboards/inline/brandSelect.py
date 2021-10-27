from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.inline.callbacks import callbackDatas

brandButtons = InlineKeyboardMarkup()
Adidas = InlineKeyboardButton(text='Adidas', callback_data=callbackDatas.brandCallBack.new(brand="adidas"))
Nike = InlineKeyboardButton(text='Nike', callback_data=callbackDatas.brandCallBack.new(brand='nike'))
NewBalance = InlineKeyboardButton(text='New Balance',
                                  callback_data=callbackDatas.brandCallBack.new(brand='newbalance'))
Converse = InlineKeyboardButton(text='Converse', callback_data=callbackDatas.brandCallBack.new(brand='converse'))
Puma = InlineKeyboardButton(text='Puma', callback_data=callbackDatas.brandCallBack.new(brand='puma'))
Reebok = InlineKeyboardButton(text='Reebok', callback_data=callbackDatas.brandCallBack.new(brand='reebook'))
DrMartens = InlineKeyboardButton(text='Dr Martens', callback_data=callbackDatas.brandCallBack.new(brand='drmartens'))
FredPerry = InlineKeyboardButton(text='Fred Perry', callback_data=callbackDatas.brandCallBack.new(brand='fredperry'))
Asics = InlineKeyboardButton(text='Asics', callback_data=callbackDatas.brandCallBack.new(brand='asics'))
Vans = InlineKeyboardButton(text='Vans', callback_data=callbackDatas.brandCallBack.new(brand='vans'))
brandButtons.add(Adidas, Asics, DrMartens, Reebok, Puma, Nike, NewBalance, Converse, Vans, FredPerry)
