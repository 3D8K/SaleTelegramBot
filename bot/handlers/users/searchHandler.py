from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode
from ...loader import dp, bot
from aiogram.utils.markdown import bold
from gui import emoji
from models.BrandModel import BrandModel
from models.RequestModel import RequestModel
from controllers.RequestController import RequestsControlelr


@dp.message_handler(text_contains="Поиск", state='*')
async def searchHandler(message: Message, state: FSMContext):
    data = await state.get_data()
    items = await RequestsControlelr.checkArrayParams(dict(data), message.chat.id)
    if (items[0] == 'err'):
        items.pop(0)
        await message.answer(
            text=bold(f"Вы не заполнили обязательные поля: {','.join((str(n) for n in items))}{emoji.WARNING_EMOJI}"),
            parse_mode=ParseMode.MARKDOWN)
    else:
        if (items == None):
            await message.answer(
                text=bold(f"К сожалению ничего не наеденно\nпопробуйте изменить параметры поиска {emoji.SAD_EMOJI}"),
                parse_mode=ParseMode.MARKDOWN)
        for s in items:
            await bot.send_photo(message.chat.id, photo=s.imgUrl, caption=s.name + '\n' + s.price + '\n' + s.url)


@dp.message_handler(text_contains="История запросов")
async def getReqHistory(message: Message):
    reqHistory = RequestModel.getRequestsInfo(message.chat.id)
    if (len(reqHistory) == 0):
        await message.answer(text=f"Ваша истрия поиска пуста{emoji.SAD_EMOJI}")
    else:
        start = len(reqHistory) - 5
        if (len(reqHistory) < 5):
            start = 0
        for i in range(start, len(reqHistory)):
            req = reqHistory[i]
            brandName = BrandModel.getBrandName(req['brand_id'])
            await message.answer(
                text=f"Бренд: {brandName}, Размер: {req['size']}, цвет: {req['color']}, цена от: {req['price_low']}, цена до: {req['price_high']}")


@dp.message_handler(text_contains="Текущие параметры поиска", state='*')
async def currentReqParams(message: Message, state: FSMContext):
    data = await state.get_data()
    if (len(data) == 0):
        await message.answer(text=bold(f"Вы еще не задали параметры поиска{emoji.WARNING_EMOJI}"),
                             parse_mode=ParseMode.MARKDOWN)
    else:
        await message.answer(text=f"Бренд: {data.get('brand')}, размер: {data.get('size')}, цвет: {data.get('color')}, минимальная цена: {data.get('priceLow')}, максимальная цена: {data.get('priceHigh')}")
