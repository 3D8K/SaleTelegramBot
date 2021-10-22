import database.database
from shops.AsosClass import Asos
from shops.LystClass import Lyst
from shops.FarfetchClass import Farfetch
from models.BrandModel import BrandModel
from models.RequestModel import RequestModel


class RequestsControlelr(object):
    @classmethod
    async def checkShops(cls, id: int, params: dict):
        await Asos.loadList()
        pass

    @classmethod
    def checkFullParams(cls, data: dict):
        emptyParams = []
        for param in data:
            if not data.get(param):
                emptyParams.append(param)
        return emptyParams
