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
    @staticmethod
    def connectDb():
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection

    @classmethod
    def createUser(cls, user_id: int, gender: int):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                addUserQuery = f"INSERT INTO `users` (telegram_tag, gender) VALUES ({user_id}, {gender})"
                cursor.execute(addUserQuery)
                connection.commit()
        except:
            print('Дубликат')
        finally:
            connection.close()

    @classmethod
    def getBrandId(cls, brand: str):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                getBrandIdQuery = f"SELECT shops_has_brands.brand_req_id, shops.`name` FROM shops_has_brands INNER JOIN shops ON shops_has_brands.shop_id = shops.shop_id " \
                                  f"INNER JOIN brands ON shops_has_brands.brand_id = brands.brand_id WHERE brands.`name` = '{brand}'"
                cursor.execute(getBrandIdQuery)
                brandIDList = cursor.fetchall()
        finally:
            connection.close()
            return brandIDList

    @classmethod
    def loggReq(cls, id: int, brand: str, color: str, size: str, priceLow: int, priceHigh: int):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                getUserBrandInfo = f"SELECT users.user_id, brands.brand_id FROM users, brands WHERE users.telegram_tag = {id} AND brands.`name` = '{brand}'"
                cursor.execute(getUserBrandInfo)
                params = cursor.fetchall()
                loggReq = f"INSERT INTO `requests` (user_id, brand_id, color, size, price_low, price_high) values ({'user_id'[params]}, {'brand_id'[params]}, '{color}', '{size}', {priceLow}, {priceHigh})"
                cursor.execute(loggReq)
                connection.commit()
        finally:
            connection.close()

    @classmethod
    def getWaitList(cls, brand: str, name: str, color: str, size: str):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                WaitListQuery = f""
                cursor.execute(WaitListQuery)
                connection.commit()
        finally:
            connection.close()

    @classmethod
    def addBrand(cls, brandName: str):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                addNewBrand = f"INSERT INTO `brands` (name) VALUE ({brandName})"
                cursor.execute(addNewBrand)
                connection.commit()
        finally:
            connection.close()

    @classmethod
    def addRequestLog(cls, id: int, brand: str, size: str, color: str, priceLow: int, priceHigh: int):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                getUserBrandInfo = f"SELECT users.user_id, brands.brand_id FROM users, brands WHERE users.telegram_tag = {id} AND brands.`name` = '{brand}'"
                cursor.execute(getUserBrandInfo)
                params = cursor.fetchall()
                requestInfo = f"INSERT INTO `requests` (user_id, brand_id, size, color, price_low, price_high) VALUES ({params['user_id']}, {params['brand_id']}, {size},{color},{priceLow},{priceHigh})"
                cursor.execute(requestInfo)
                connection.commit()
        finally:
            connection.close()

    @classmethod
    def getRequestLog(cls, id: int):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                getUserBrandInfo = f"SELECT users.user_id FROM users WHERE users.telegram_tag = {id}"
                cursor.execute(getUserBrandInfo)
                userId = cursor.fetchall()
                getUserBrandInfo = f"SELECT * FROM `requests` WHERE user_id = {userId['user_id']}"
                cursor.execute(getUserBrandInfo)
                info = cursor.fetchall()
        finally:
            connection.close()
            return info

    @classmethod
    def changeParam(cls, id: int, tableName: str, collum: str, newValue):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                if (newValue is str):
                    changeValue = f"UPDATE `{tableName}` SET {collum} = '{newValue}' WHERE id={id}"
                else:
                    changeValue = f"UPDATE `{tableName}` SET {collum} = {newValue} WHERE id={id}"
                cursor.execute(changeValue)
                connection.commit()
        finally:
            connection.close()

    @classmethod
    def addItem(cls, brand: str, modelName: str, color: str, size: str):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                getBrandId = f"SELECT brands.brand_id FROM brands WHERE brands.name = '{brand}'"
                cursor.execute(getBrandId)
                brandId = cursor.fetchall()
                addItemRequest = f"INSERT INTO `items` (brand_id, name, color, size) VALUES ({brandId}, '{modelName}',{color}, {size})"
                cursor.execute(addItemRequest)
        finally:
            connection.close()
