from shops.AsosClass import Asos
from models.BrandModel import BrandModel


class RequestsControlelr(object):
    def checkShops(self, id: int, brand: str):
        SneakerList = []
        BrandList = BrandModel()
        BrandList = BrandModel.getBrandIds(self=BrandList, brand=brand)
        for item in Asos.loadList(Asos, params['gender'], BrandList[0]['brand_req_id'], colors[color], params['priceLow'],
                                  params['priceHigh'], float(params['size'])):
            SneakerList.append(item)
        return BrandList

    def checkDialog(self, id: int):
        pass


