from aiogram import Bot, Dispatcher, types
from configurate.configurate import token
import logging

bot = Bot(token=token)
dp = Dispatcher(bot)

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )
