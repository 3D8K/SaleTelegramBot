from models.core.Model import Model
from models.BrandModel import BrandModel
from models.UserModel import UserModel
from database.database import Database


class RequestModel(Model):
    tableName = 'requests'

    def __init__(self, telegrmId: int, brand: str, size: str, color: str, priceLow: int, priceHigh: int):
        userId = UserModel.getUserId(telegrmId)
        brandId = BrandModel.getBrandid(brand)
        columns = 'user_id', 'brand_id', 'size', 'color', 'price_low', 'price_high'
        values = userId, brandId, size, color, priceLow, priceHigh
        Database.add(self.tableName, columns, values)

    @classmethod
    def getRequestsInfo(cls, telegramId: int):
        userId = UserModel.getUserId(telegramId)
        return Database.checkLine(cls.tableName, 'user_id', userId)
