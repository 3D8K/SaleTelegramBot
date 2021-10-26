from models.core.Model import Model
from database.database import Database


class ShopModel(Model):
    tableName = 'shops'

    def __init__(self, name: str):
        Database.add(self.tableName, 'name', name)

    @classmethod
    def getShopId(cls, shopName):
        result = Database.checkLine(cls.tableName, 'name', shopName)[0]
        return result.get('shop_id')
