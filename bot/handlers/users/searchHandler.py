from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode
from ...loader import dp, bot
from aiogram.utils.markdown import bold
from gui import emoji
from models.RequestModel import RequestModel
from controllers.RequestController import RequestsControlelr


@dp.message_handler(text_contains="Поиск", state='*')
async def searchHandler(message: Message, state: FSMContext):
    data = await state.get_data()
    items = await RequestsControlelr.checkArrayParams(dict(data))
    if (items[0] == 'err'):
        items.pop(0)
        await message.answer(
            text=bold(f"Вы не заполнили обязательные поля:{','.join((str(n) for n in items))}{emoji.WARNING_EMOJI}"),
            parse_mode=ParseMode.MARKDOWN)
    else:
        if (items == None):
            await message.answer(
                text=bold(f"К сожалению ничего не наеденно\nпопробуйте изменить параметры поиска {emoji.SAD_EMOJI}"),
                parse_mode=ParseMode.MARKDOWN)
        for s in items:
            await bot.send_photo(message.chat.id, photo=s.imgUrl, caption=s.name + '\n' + s.price + '\n' + s.url)
