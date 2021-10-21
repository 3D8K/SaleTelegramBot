from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode
from aiogram.utils.markdown import  bold,  code
from ...loader import dp, bot
from ...keyboards.reply.priceMenu import priceButtons
from ...keyboards.reply.mainMenu import mainMenuButtons
from ...states.SearchParamsClass import SearchParams


@dp.message_handler(text_contains="Цена")
async def priceMenu(message: Message):
    await message.answer(text=bold('Меню цен\n'), parse_mode=ParseMode.MARKDOWN, reply_markup=priceButtons)


@dp.message_handler(text_contains='Назад')
async def goToMainMenu(message: Message):
    await message.answer(text='Главное меню', reply_markup=mainMenuButtons)


@dp.message_handler(text_contains='До')
async def setPriceHigh(message: Message):
    await message.answer(text=bold('Введите цену до\n')+code('для активации других пунктов завершите выбор'), parse_mode=ParseMode.MARKDOWN)
    await SearchParams.PRICE_HIGH.set()


@dp.message_handler(state=SearchParams.PRICE_HIGH)
async def getPriceHigh(message: Message, state: FSMContext):
    priceHigh = message.text
    await state.update_data(priceLow=priceHigh)
    await state.reset_state(with_data=False)


@dp.message_handler(text_contains='От')
async def setPriceLow(message: Message):
    await message.answer(text=bold('Введите цену от\n')+code('для активации других пунктов завершите выбор'), parse_mode=ParseMode.MARKDOWN)
    await SearchParams.PRICE_LOW.set()


@dp.message_handler(state=SearchParams.PRICE_LOW)
async def getPriceLow(message: Message, state: FSMContext):
    priceLow = message.text
    await state.update_data(priceHigh=priceLow)
    await state.reset_state(with_data=False)
