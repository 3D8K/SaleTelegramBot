from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from ...loader import dp
from controllers.RequestController import RequestsControlelr



@dp.message_handler(text_contains="Поиск", state='*')
async def printState(message: Message, state: FSMContext):
    data = await state.get_data()
    RequestsControlelr.checkFullParams(dict(data))
