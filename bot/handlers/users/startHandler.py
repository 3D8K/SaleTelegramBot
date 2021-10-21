from aiogram.types import Message, CallbackQuery
from ...keyboards.inline import genderSelect
from ...keyboards.reply.buttonsReply import mainMenuButtons
from ...loader import dp, bot
from database.database import Database


@dp.message_handler(commands='start')
async def startFunction(message: Message):
    if (Database.checkRegistration(message.chat.id)):
        await message.answer(text='С возвращением {0.first_name}!'.format(message.from_user),
                             reply_markup=mainMenuButtons)
    else:
        await message.answer(text='Привет, {0.first_name}\nВыберете свой пол для регестарции'.format(message.from_user),
                             reply_markup=genderSelect.genderButtons)


@dp.callback_query_handler(text_contains="genderSelect")
async def selectGender(call: CallbackQuery):
    if ('men' in call.data):
        Database.createUser(call.from_user.id, 1)
    else:
        Database.createUser(call.from_user.id, 0)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спасибо за регестарцию!", reply_markup=None)
