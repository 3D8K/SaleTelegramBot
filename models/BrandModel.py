from models.Model import Model
from database.database import Database


class BrandModel(Model):
    def __init__(self, brandName: str):
        addNewBrand = Database()
        addNewBrand.addBrand(brandName)

    @classmethod
    def getBrandIds(cls, brand: str):
        listBrandId = Database.getBrandId('adidas')
        return listBrandId
