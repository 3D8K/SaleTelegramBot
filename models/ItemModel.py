from models.Model import Model
from database.database import Database


class ItemModel(Model):
    def __init__(self, brand: str, modelName: str, color: str, size: str):
        Database.addItem(brand, modelName, color, size)

