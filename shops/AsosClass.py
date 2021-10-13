from shops.ShopClass import Shop


class Asos(Shop):
    def loadList(self, gender: int, brand: int, color: str, priceLow: int, priceHigh: int, size: str):
        requestParams = {'brand': brand, 'base_color': color[colors], 'channel': 'desktop-web', 'country': 'RU',
                         'currency': 'RUB', 'discount_band': 2,
                         'keyStoreDataversion': 'hgk0y12-29', 'lang': 'ru-RU', 'limit': 100, 'offset': -100,
                         'priceMax': priceHigh, 'priceMin': priceLow, 'rowlength': 4, 'size': size,
                         'store': 'RU'}

    def jsonPars(self, jsonlist: dict):
        pass
