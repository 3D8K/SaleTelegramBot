from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from ...loader import dp
from controllers.RequestController import RequestsControlelr

@dp.message_handler(text_contains="Поиск", state='*')
async def searchHandler(message: Message, state: FSMContext):
    data = await state.get_data()
    await RequestsControlelr.checkArrayParams(dict(data))
