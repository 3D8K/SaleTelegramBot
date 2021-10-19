from models.Model import Model
from database.database import Database


class UserModel(Model):
    def __init__(self, userId: int, gender: int):
        AddUser = Database.createUser(userId, gender)

    @classmethod
    def changeGender(cls, id: int, newGender: int):
        Database.changeParam(id, 'users', 'gender', newGender)

    @classmethod
    def checkUser(cls,id: int):
        if(Database.checkRegistration(id)):
            return True
        else:
            return False

