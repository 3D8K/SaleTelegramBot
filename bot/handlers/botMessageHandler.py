from bot.bot import bot
from bot.buttons import buttonsReply
from models.UserModel import UserModel


@bot.message_handler(commands=['start'])
def startFunction(message):
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}\nВыберете свой пол для регестарции'.format(message.from_user),
                     reply_markup=buttonsReply.genderButtons)


@bot.callback_query_handler(func=lambda call: True)
def callbackHandler(call):
    if ('gender' in call.data):
        if (call.data == 'genderMen'):
            gender = 1
        else:
            gender = 0
        UserModel(call.from_user.id, gender)
        bot.edit_message_text('Спасибо за регистарцию!', chat_id=call.message.chat.id,
                              message_id=call.message.id, reply_markup=None)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as error:
            print(error)
