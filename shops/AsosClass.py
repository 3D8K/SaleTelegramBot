from shops.ShopClass import Shop
from colors import asosColors
from fake_useragent import UserAgent
import requests
from SneakerClass import Sneaker


class Asos(Shop):
    def loadList(self, gender: int, brand: int, color: str, priceLow: int, priceHigh: int, size: str):
        if (gender):
            url = 'https://www.asos.com/api/product/search/v2/categories/4209?'
        else:
            url = 'https://www.asos.com/api/product/search/v2/categories/4172?'

        requestParams = {'brand': brand, 'base_color': color[asosColors], 'channel': 'desktop-web', 'country': 'RU',
                         'currency': 'RUB', 'discount_band': 2,
                         'keyStoreDataversion': 'hgk0y12-29', 'lang': 'ru-RU', 'limit': 100, 'offset': -100,
                         'priceMax': priceHigh, 'priceMin': priceLow, 'rowlength': 4, 'size': size,
                         'store': 'RU'}
        uaTemp = UserAgent()
        randomUserAgent = uaTemp.random
        req = requests.get(url=url, params=requestParams, headers={"User-Agent": randomUserAgent})
        try:
            response = req.json()
        except:
            return []
        self.jsonPars(response)


    def jsonPars(self, jsonList: dict):
        productList = []
        for product in jsonList['products']:
            name = product['name']
            productList.append(Sneaker(name[name.find(product['brandName']):], product['price']['current']['text'],
                                                    ('https://www.asos.com/ru/' + product['url']),
                                                    'https://' + product['imageUrl']))
        return productList
