from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import  bold,  code
from aiogram.types import Message, CallbackQuery, ParseMode
from ...loader import dp, bot
from gui.emoji import *
from ...keyboards.inline.colorSelect import colorsButton
from ...states.SearchParamsClass import SearchParams


@dp.message_handler(text_contains="Цвет")
async def selectBrand(message: Message):
    await message.answer(text=bold('Выберете цвет\n')+code('для активации других пунктов завершите выбор'), parse_mode=ParseMode.MARKDOWN,reply_markup=colorsButton)
    await SearchParams.COLOR.set()


@dp.callback_query_handler(text_contains='colorSelect', state=SearchParams.COLOR)
async def brandSelect(call: CallbackQuery, state: FSMContext):
    colors = {'white': f'{WHITE_EMOJI}', 'black': f'{BLACK_EMOJI}', 'brown': f'{BROWN_EMOJI}', 'red': f'{RED_EMOJI}',
              'orange': f'{ORANGE_EMOJI}', 'yellow': f'{YELLOW_EMOJI}',
              'purple': f'{PURPLE_EMOJI}', 'blue': f'{BLUE_EMOJI}', 'green': f'{GREEN_EMOJI}', 'any': 'любой'}
    color = call.data.split(':', 1)[1]
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f"Вы выбрали {colors[color]} цвет", reply_markup=None)
    await state.update_data(color=color)
    await state.reset_state(with_data=False)
