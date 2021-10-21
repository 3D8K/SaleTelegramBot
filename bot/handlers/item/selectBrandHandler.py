from aiogram.types import Message
from ...loader import dp
from ...keyboards.inline.brandSelect import brandButtons


@dp.message_handler(text_contains="Бренд")
async def selectBrand(message: Message):
    await message.answer(text='Выберете бренд', reply_markup=brandButtons)
