from database.database import Database
from models.core.Model import Model


class BrandModel(Model):
    tableName = 'brands'
    column = 'name'
    coherentTableName = 'shops_has_brands'
    coherentColumn = 'brand_id'

    def __init__(self, brandName: str):
        Database.add(self.tableName, self.column, brandName)

    @classmethod
    def getBrandid(cls, brand: str):
        brandId = Database.checkLine(cls.tableName, cls.column, brand)
        return brandId[0]['brand_id']

    @classmethod
    def getBrandIds(cls, brand: str):
        brandId = cls.getBrandid(brand)
        listBrandId = Database.checkLine(cls.coherentTableName, cls.coherentColumn, brandId)
        return listBrandId

    @classmethod
    def getBrandName(cls,brandId:str):
        brandName = Database.checkLine(cls.tableName,cls.coherentColumn, brandId)
        return brandName[0]['name']