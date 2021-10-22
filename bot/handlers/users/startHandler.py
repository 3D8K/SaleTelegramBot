from aiogram.types import Message, CallbackQuery, ParseMode
from aiogram.utils.markdown import bold
from models.UserModel import UserModel
from ...keyboards.inline import genderSelect
from ...keyboards.reply.mainMenu import mainMenuButtons
from ...loader import dp, bot


@dp.message_handler(commands='start')
async def startFunction(message: Message):
    if (UserModel.checkUser(message.chat.id)):
        await message.answer(text='С возвращением {0.first_name}!'.format(message.from_user),
                             reply_markup=mainMenuButtons)
    else:
        await message.answer(text='Привет, {0.first_name}\nВыберете свой пол для регестарции'.format(message.from_user),
                             reply_markup=genderSelect.genderButtons)


@dp.callback_query_handler(text_contains="genderSelect")
async def selectGender(call: CallbackQuery):
    if ('women' in call.data):
        UserModel(call.from_user.id, 0)
    else:
        UserModel(call.from_user.id, 1)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Спасибо за регестрацию!',reply_markup=None)
    await bot.send_message(chat_id=call.message.chat.id, text=bold('Главное меню'), reply_markup=mainMenuButtons)
