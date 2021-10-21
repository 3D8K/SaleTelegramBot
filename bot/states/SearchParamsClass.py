from aiogram.dispatcher.filters.state import StatesGroup, State

class SearchParams(StatesGroup):
    GENDER = State()
    COLOR = State()
    SIZE = State()
    BRAND = State()
    PRICE_LOW = State()
    PRICE_HIGH = State()