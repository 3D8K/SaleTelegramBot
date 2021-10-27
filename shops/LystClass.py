import requests

from models.core.ShopClass import Shop
from models.core.SneakerClass import Sneaker


class Lyst(Shop):
    @classmethod
    def loadList(cls, gender, brand: str, color, priceLow, priceHigh, size):
        brand = brand.lower().replace(' ', '-')
        if (brand == 'drmartens'):
            color = 'black'
        if (brand == 'asics'):
            brand = 'asicsr'
        if (color == 'any'):
            color = 'multicolor'
        if (gender):
            url = f"https://www.lyst.com/api/rothko/modules/product_feed/?url=https%3A%2F%2Fwww.lyst.com%2Fshop%2Fmens-{brand}-shoes%2F%3Fcolor%3D{color}%26final_price_from%3D{priceLow}%26final_price_to%3D{priceHigh}%26size%3DIT%2B{size}%26page%3D2"
        else:
            url = f"https://www.lyst.com/api/rothko/modules/product_feed/?url=https%3A%2F%2Fwww.lyst.com%2Fshop%2F{brand}-shoes%2F%3Fcolor%3D{color}%26final_price_to%3D{priceHigh}%26instock_size%3Dsize.footwear.eu.u.{size}%26page-1"
        req = requests.get(url=url)
        try:
            response = req.json()
        except:
            sneakerList = []
            return sneakerList
        jsonList = response['data']['feed_items']
        return cls.jsonPars(jsonList)

    @classmethod
    def jsonPars(cls, jsonList):
        SneakerList = []
        for item in jsonList:
            SneakerList.append(Sneaker(name=item['product_card']['image_alt_text'],
                                       price=item['product_card']['sale_price_with_currency_symbol'] or
                                             item['product_card']['full_price_with_currency_symbol'],
                                       url='https://www.lyst.com' + item['product_card']['url'],
                                       imgUrl=item['product_card']['image_url']))
        return SneakerList
