from shops.AsosClass import Asos
from shops.LystClass import Lyst
from shops.FarfetchClass import Farfetch
from models.BrandModel import BrandModel
from models.RequestModel import RequestModel


class RequestsControlelr(object):
    @classmethod
    async def checkShops(cls, brandIds: dict, params: dict):
        gender = params['gender']
        brand_id = brandIds[0]['brand_req_id']
        color = params['color']
        priceLow = params['priceLow']
        priceHigh = params['priceHigh']
        size = params['size']

        await Asos.loadList(params['gender'], brand_id, params['color'], params['priceLow'],
                            params['priceHigh'], params['size'])
        pass

    @classmethod
    async def checkArrayParams(cls, data: dict):
        emptyKeys = []
        if data.setdefault('priceLow') == None:
            data['priceLow'] = 0
        if data.setdefault('priceHigh') == None:
            data['priceHigh'] = 99999999
        if data.setdefault('color') == None:
            data['color'] = 'any'
        if len(data) < 6:
            if 'gender' not in data:
                emptyKeys.append('gender')
            if 'brand' not in data:
                emptyKeys.append('brand')
            if 'size' not in data:
                emptyKeys.append('size')


        else:
            brandsId = BrandModel.getBrandIds(data['brand'])
            await cls.checkShops(brandsId, data)
