from abc import abstractmethod

from models.core.Model import Model


class Shop(Model):
    @abstractmethod
    def loadList(self, gender: int, brand: int, color: str, priceLow: int, priceHigh: int, size: str):
        pass

    @abstractmethod
    def jsonPars(self, jsonlist: dict):
        pass
