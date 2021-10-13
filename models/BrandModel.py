from models.Model import Model
from database.database import Database


class BrandModel(Model):
    def getBrandIds(self, brand: str):
        listBrandId = Database()
        listBrandId = Database.getBrandId(listBrandId, brand)
        return listBrandId
