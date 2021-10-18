from models.Model import Model
from abc import  abstractmethod


class Shop(Model):
    @abstractmethod
    def loadList(self, gender: int, brand: int, color: str, priceLow: int, priceHigh: int, size: str):
        pass

    @abstractmethod
    def jsonPars(self, jsonlist: dict):
        pass
