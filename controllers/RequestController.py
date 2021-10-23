from shops.AsosClass import Asos
from shops.LystClass import Lyst
from shops.FarfetchClass import Farfetch
from models.BrandModel import BrandModel
from models.RequestModel import RequestModel


class RequestsControlelr(object):
    @classmethod
    def checkShops(cls, brandIds: dict, params: dict):
        resultAsos = Asos.loadList(params['gender'], brandIds[0]['brand_req_id'], params['color'],
                                   params['priceLow'],
                                   params['priceHigh'], params['size']),
        resultFarfetch = Farfetch.loadList(params['gender'], brandIds[1]['brand_req_id'], params['color'],
                                           params['priceLow'],
                                           params['priceHigh'], params['size'])
        result = resultAsos[0] + resultFarfetch
        return result

    @classmethod
    async def checkArrayParams(cls, data: dict):
        emptyKeys = ['err']
        if data.setdefault('priceLow') == None:
            data['priceLow'] = 0
        if data.setdefault('priceHigh') == None:
            data['priceHigh'] = 99999999
        if data.setdefault('color') == None:
            data['color'] = 'any'
        if len(data) < 6:
            if 'gender' not in data:
                emptyKeys.append('пол')
            if 'brand' not in data:
                emptyKeys.append('бренд')
            if 'size' not in data:
                emptyKeys.append('размер')
            return emptyKeys

        else:
            brandsId = BrandModel.getBrandIds(data['brand'])
            return cls.checkShops(brandsId, data)
