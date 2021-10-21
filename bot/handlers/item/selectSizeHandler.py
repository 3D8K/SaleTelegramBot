from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from ...loader import dp, bot
from ...keyboards.inline.sizeSelect import sizeButtons
from ...states.SearchParamsClass import SearchParams

@dp.message_handler(text_contains="Размер")
async def selectBrand(message: Message):
    await message.answer(text='Выберете размер', reply_markup=sizeButtons)
    await SearchParams.SIZE.set()

@dp.callback_query_handler(text_contains='sizeSelect', state=SearchParams.SIZE)
async def brandSelect(call: CallbackQuery, state: FSMContext):
    size = call.data.split(':', 1)[1]
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Вы выбрали {size} размер", reply_markup=None)
    await state.update_data(size=size)
    await state.reset_state(with_data=False)
