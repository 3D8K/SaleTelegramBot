from models.Model import Model
from database.database import Database


class RequestModel(Model):
    def __init__(self, id: int, brand: str, size: str, color: str, priceLow: int, priceHigh: int):
        Database.addRequestLog(id, brand, size, color, priceLow, priceHigh)

    @classmethod
    def getRequestsInfo(cls, id: int):
        return Database.getRequestLog(id)


