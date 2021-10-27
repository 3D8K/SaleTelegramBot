from aiogram.types import ParseMode
from bot.loader import bot
from aiogram.utils.markdown import bold
from gui import emoji
from shops.AsosClass import Asos
from shops.LystClass import Lyst
from shops.FarfetchClass import Farfetch
from models.BrandModel import BrandModel
from models.RequestModel import RequestModel
LEN_ARRAY_PARAMS = 6
MAX_PRICE_DEFAULT = 100000
MIN_PRICE_DEFAULT = 0


class RequestsControlelr(object):
    @classmethod
    def checkShops(cls, brandIds: dict, brandName: str, params: dict):
        resultAsos = Asos.loadList(params['gender'], brandIds[0]['brand_req_id'], params['color'],
                                   params['priceLow'],
                                   params['priceHigh'], params['size']),
        resultFarfetch = Farfetch.loadList(params['gender'], brandIds[1]['brand_req_id'], params['color'],
                                           params['priceLow'],
                                           params['priceHigh'], params['size'])
        resultLyst = Lyst.loadList(params['gender'], brandName, params['color'],
                                   params['priceLow'],
                                   params['priceHigh'], params['size'])
        result = resultAsos[0] + resultFarfetch + resultLyst
        return result

    @classmethod
    async def checkArrayParams(cls, data: dict, telegaramTag: int):
        emptyKeys = ['err']
        if data.setdefault('priceLow') == None:
            data['priceLow'] = MIN_PRICE_DEFAULT
        if data.setdefault('priceHigh') == None:
            data['priceHigh'] = MAX_PRICE_DEFAULT
        if data.setdefault('color') == None:
            data['color'] = 'any'
        if len(data) < LEN_ARRAY_PARAMS:
            if 'gender' not in data:
                emptyKeys.append('пол')
            if 'brand' not in data:
                emptyKeys.append('бренд')
            if 'size' not in data:
                emptyKeys.append('размер')
            return emptyKeys

        else:
            await bot.send_message(chat_id=telegaramTag,
                                   text=bold(f"Выполняю поиск {emoji.WAIT_EMOJI}"),
                                   parse_mode=ParseMode.MARKDOWN)
            RequestModel(telegaramTag, data['brand'], data['size'], data['color'], data['priceLow'], data['priceHigh'])
            brandsId = BrandModel.getBrandIds(data['brand'])
            return cls.checkShops(brandIds=brandsId, params=data, brandName=data['brand'])
