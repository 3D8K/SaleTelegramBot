from models.Model import Model
from database.database import Database


class UserModel(Model):
    tableName = 'users'
    ColumnName = 'telegram_tag'

    def __init__(self, userId: int, gender: int):
        params = 'telegram_tag', 'gender'
        values = userId, gender
        Database.add(self.tableName, params, values)

    @classmethod
    def getUserId(cls, telegramId: int):
        result = Database.checkLine(cls.tableName, cls.ColumnName, telegramId)[0]
        return result.get('user_id')

    @classmethod
    def changeGender(cls, id: int, newGender: int):
        collum = 'gender'
        Database.change(cls.tableName, collum, newGender, cls.ColumnName, id)

    @classmethod
    def checkUser(cls, id: int):
        if (Database.checkLine(cls.tableName, cls.ColumnName, id)):
            return True
        else:
            return False


