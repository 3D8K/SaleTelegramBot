from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from ...loader import dp, bot
from ...keyboards.inline.genderSelect import genderButtons
from ...states.SearchParamsClass import SearchParams

@dp.message_handler(text_contains="Пол")
async def selectBrand(message: Message):
    await message.answer(text='Выберете размерную сетку', reply_markup=genderButtons)
    await SearchParams.GENDER.set()

@dp.callback_query_handler(text_contains='genderSelect', state=SearchParams.GENDER)
async def brandSelect(call: CallbackQuery, state: FSMContext):
    gender = call.data.split(':', 1)[1]
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Вы выбрали {gender} размерную сетку", reply_markup=None)
    await state.update_data(gender=gender)
    await state.reset_state(with_data=False)
