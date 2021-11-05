import requests
from fake_useragent import UserAgent

from gui.fatfetchGui.FarfetchArrayParams import *
from models.core.ShopClass import Shop
from models.core.SneakerClass import Sneaker


class Farfetch(Shop):
    @classmethod
    def loadList(cls, gender, brand, color, priceLow, priceHigh, size):
        if (gender):
            gender = 'Men'
        else:
            gender = 'Women'
        url = 'https://www.farfetch.com/ru/plpslice/listing-api/products-facets?'
        requestParams = {'view': 250, 'scale': 282, 'rootCategory': gender, 'pagetype': 'Shopping',
                         'pricetype': 'fullprice', 'c-category': 137174,
                         'c-designer': brand, 'size': sizes[float(size)], 'colour': colors[color],
                         'price': str(int(priceLow)) + '-' + str(int(priceHigh))}
        uaTemp = UserAgent()
        randomUserAgent = uaTemp.random
        req = requests.get(url=url, params=requestParams, headers={"User-Agent": randomUserAgent})
        try:
            responese = req.json()
        except:
            randomUserAgent = uaTemp.random
            req = requests.get(url=url, params=requestParams, headers={"User-Agent": randomUserAgent})
            try:
                responese = req.json()
            except:
                return []
        sneakerList = responese['listingItems']['items']
        return cls.jsonPars(sneakerList)

    @classmethod
    def jsonPars(cls, jsonList):
        productList = []
        for product in jsonList:
            productList.append(Sneaker(product['brand']['name'] + ' ' + product['shortDescription'],
                                       product['priceInfo']['formattedFinalPrice'],
                                       'https://www.farfetch.com/' + product['url'],
                                       product['images']['model']))
        return productList
