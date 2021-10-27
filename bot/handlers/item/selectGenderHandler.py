from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ParseMode
from aiogram.utils.markdown import bold, code

from ...keyboards.inline.genderSelect import genderButtons
from ...loader import dp, bot
from ...states.SearchParamsClass import SearchParams


@dp.message_handler(text_contains="Пол")
async def selectBrand(message: Message):
    await message.answer(text=bold('Выберете размерную сетку\n') + code('для активации других пунктов завершите выбор'),
                         parse_mode=ParseMode.MARKDOWN, reply_markup=genderButtons)
    await SearchParams.GENDER.set()


@dp.callback_query_handler(text_contains='genderSelect', state=SearchParams.GENDER)
async def brandSelect(call: CallbackQuery, state: FSMContext):
    if (call.data.split(':', 1)[1] == 'men'):
        gender = 'мужскую'
        await state.update_data(gender=1)
    else:
        gender = 'женскую'
        await state.update_data(gender=0)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f"Вы выбрали {gender} размерную сетку", reply_markup=None)
    await state.reset_state(with_data=False)
