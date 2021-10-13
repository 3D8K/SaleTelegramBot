import pymysql
from database.configDB import *


class SingletonMeta(type):
    _instances = {}

    def __call__(cls):
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def connectDb(self):
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection

    def createUser(self, user_id: int, gender: int):
        connection = self.connectDb()
        try:
            with connection.cursor() as cursor:
                addUserQuery = f"INSERT INTO `users` (telegram_tag, gender) VALUES ({user_id}, {gender})"
                cursor.execute(addUserQuery)
                connection.commit()
        except:
            print('Дубликат')
        finally:
            connection.close()

    def getBrandId(self, brand: str):
        connection = self.connectDb()
        try:
            with connection.cursor() as cursor:
                getBrandIdQuery = f"SELECT shb.brand_req_id,sh.name FROM shops_has_brands as shb JOIN shops as sh JOIN brands as b on b.brand_id =shb.brand_id WHERE b.name = '{brand}' and shb.shop_id = sh.shop_id"
                cursor.execute(getBrandIdQuery)
                brandIDList = cursor.fetchall()
        finally:
            connection.close()
            return brandIDList

    def loggReq(self, user_id: int, brand: str, color: str, size: str,priceLow: int, priceHigh: int):
        connection = self.connectDb()
        try:
            with connection.cursor() as cursor:
                loggReqQuery = f""
                cursor.execute(loggReqQuery)
                connection.commit()
        finally:
            connection.close()

    def getWaitList(self, brand: str, name: str, color: str, size: str):
        connection = self.connectDb()
        try:
            with connection.cursor() as cursor:
                WaitListQuery = f""
                cursor.execute(WaitListQuery)
                connection.commit()
        finally:
            connection.close()


if __name__ == '__main__':
    Test = Database()
    Info = Database.getBrandId(Test, 'adidas')
    print(*Info)
