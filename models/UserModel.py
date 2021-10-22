from models.Model import Model
from database.database import Database


class UserModel(Model):
    tableName = 'users'
    idColumnName = 'telegram_tag'

    def __init__(self, userId: int, gender: int):
        params = 'telegram_tag', 'gender'
        values = userId, gender
        Database.add(self.tableName, params, values)

    @classmethod
    def changeGender(cls, id: int, newGender: int):
        collum = 'gender'
        Database.change(cls.tableName, collum, newGender, cls.idColumnName, id)

    @classmethod
    def checkUser(cls, id: int):
        if (Database.checkLine(cls.tableName, cls.idColumnName, id)):
            return True
        else:
            return False

