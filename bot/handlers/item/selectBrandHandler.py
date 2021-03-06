from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ParseMode
from aiogram.utils.markdown import bold, code

from ...keyboards.inline.brandSelect import brandButtons
from ...loader import dp, bot
from ...states.SearchParamsClass import SearchParams


@dp.message_handler(text_contains="Бренд")
async def selectBrand(message: Message):
    await message.answer(text=bold('Выберете бренд\n')+code('для активации других пунктов завершите выбор'), reply_markup=brandButtons, parse_mode=ParseMode.MARKDOWN)
    await SearchParams.BRAND.set()

@dp.callback_query_handler(text_contains='brandSelect', state=SearchParams.BRAND)
async def brandSelect(call: CallbackQuery, state: FSMContext):
    brand = call.data.split(':', 1)[1]
    await state.update_data(brand=brand)
    await state.reset_state(with_data=False)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Вы выбрали бренд {brand}", reply_markup=None)


