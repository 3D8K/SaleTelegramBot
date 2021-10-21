from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from ...loader import dp, bot
from ...keyboards.inline.colorSelect import colorsButton
from ...states.SearchParamsClass import SearchParams

@dp.message_handler(text_contains="Цвет")
async def selectBrand(message: Message):
    await message.answer(text='Выберете цвет', reply_markup=colorsButton)
    await SearchParams.COLOR.set()

@dp.callback_query_handler(text_contains='colorSelect', state=SearchParams.COLOR)
async def brandSelect(call: CallbackQuery, state: FSMContext):
    color = call.data.split(':', 1)[1]
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Вы выбрали {color} цвет", reply_markup=None)
    await state.update_data(color=color)
    await state.reset_state(with_data=False)
