from aiogram.types import Message
from ...keyboards.inline import startSelectButtons
from ...keyboards.reply.buttonsReply import mainMenuButtons
from ...loader import dp
from database.database import Database

@dp.message_handler(commands='start')
async def startFunction(message: Message):
    if (Database.checkRegistration(message.chat.id)):
        await message.answer(text='С возвращением {0.first_name}!'.format(message.from_user), reply_markup=mainMenuButtons)
    else:
        await message.answer(text='Привет, {0.first_name}\nВыберете свой пол для регестарции'.format(message.from_user),
                             reply_markup=startSelectButtons.genderButtons)
