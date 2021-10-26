from models.core.ShopClass import Shop
from gui.colors import asosColors
from fake_useragent import UserAgent
import requests
from gui.asosGui.AsosArrayParams import *
from models.core.SneakerClass import Sneaker


class Asos(Shop):
    @classmethod
    def loadList(cls, gender, brand, color, priceLow, priceHigh, size):
        if (brand == 18):
            sizes = adidasSizes
        else:
            sizes = sizesArr
        if (gender):
            url = 'https://www.asos.com/api/product/search/v2/categories/4209?'
        else:
            url = 'https://www.asos.com/api/product/search/v2/categories/4172?'

        requestParams = {'brand': brand, 'base_color': asosColors[color], 'channel': 'desktop-web', 'country': 'RU',
                         'currency': 'RUB', 'discount_band': 2,
                         'keyStoreDataversion': 'hgk0y12-29', 'lang': 'ru-RU', 'limit': 100, 'offset': -100,
                         'priceMax': priceHigh, 'priceMin': priceLow, 'rowlength': 4, 'size': sizes[float(size)],
                         'store': 'RU'}
        uaTemp = UserAgent()
        randomUserAgent = uaTemp.random
        req = requests.get(url=url, params=requestParams)
        try:
            response = req.json()
        except:
            return []
        return cls.jsonPars(response)

    @classmethod
    def jsonPars(cls, jsonList: dict):
        productList = []
        for product in jsonList['products']:
            name = product['name']
            productList.append(Sneaker(name[name.find(product['brandName']):], product['price']['current']['text'],
                                       ('https://www.asos.com/ru/' + product['url']),
                                       'https://' + product['imageUrl']))
        return productList
