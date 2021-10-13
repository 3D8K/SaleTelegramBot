from models.Model import Model
from abc import ABC, abstractmethod


class Shop(Model, ABC):
    @abstractmethod
    def loadList(self, gender: int, brand: int, color: str, priceLow: int, priceHigh: int, size: str):
        pass

    @abstractmethod
    def jsonPars(self, jsonlist: dict):
        pass
