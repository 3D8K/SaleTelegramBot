from models.Model import Model
from database.database import Database
from models.BrandModel import BrandModel


class ItemModel(Model):
    tableName = 'items'

    def __init__(self, brand: str, modelName: str, color: str, size: str):
        brandId = Database.checkLine('brands', 'name', brand)
        columns = 'brand_id', 'name', 'color', 'size'
        values = brandId, modelName, color, size
        Database.add(self.tableName, columns, values)
