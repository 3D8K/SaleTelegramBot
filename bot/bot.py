import telebot
from configurate import configurate

bot = telebot.TeleBot(configurate.config['token'])
print(bot.get_me())
