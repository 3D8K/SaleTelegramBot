from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from ...loader import dp, bot
from gui import emoji
from controllers.RequestController import RequestsControlelr

@dp.message_handler(text_contains="Поиск", state='*')
async def searchHandler(message: Message, state: FSMContext):
    data = await state.get_data()
    items = await RequestsControlelr.checkArrayParams(dict(data))
    if (items==None):
        await message.answer(text=f"К сожалению ничего не наеденно\nпопробуйте изменить параметры поиска {emoji.SAD_EMOJI}")
    for s in items:
        await bot.send_photo(message.chat.id, photo=s.imgUrl, caption=s.name + '\n' + s.price + '\n' + s.url)
