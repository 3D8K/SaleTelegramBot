from shops.FarfetchClass import Farfetch
from shops.AsosClass import Asos
from shops.LystClass import Lyst
from models.BrandModel import BrandModel

class RequestsControlelr(object):
    def checkShops(self,id: int, brand: str):
        SneakerList = []
        BrandList = BrandModel()
        BrandList = BrandModel.getBrandIds(self=BrandList, brand=brand)

    def checkDialog(self, id: int):
        pass

if __name__ == '__main__':
    l = RequestsControlelr()
    l.checkShops(l,'adidas')