import pymysql

from configDB import *


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
    def add(cls, tableName, columns, values):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                Query = f"INSERT INTO `{tableName}` (" + ','.join((str(n) for n in columns)) + ") VALUES(" + ','.join((str(f"'{n}'") for n in values)) + ")"
                cursor.execute(Query)
                connection.commit()
        finally:
            connection.close()

    @classmethod
    def change(cls, tableName: str, column, newValue, ColumnName, value):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                Query = f"UPDATE `{tableName}` SET {column} = {newValue} WHERE {ColumnName}={value}"
                cursor.execute(Query)
                connection.commit()
        finally:
            connection.close()

    @classmethod
    def checkLine(cls, tableName, columnName, value):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                if (value == str):
                    Query = f"SELECT * FROM `{tableName}` WHERE {columnName}='{value}'"
                else:
                    Query = f"SELECT * FROM `{tableName}` WHERE {columnName}='{value}'"
                cursor.execute(Query)
                result = cursor.fetchall()
        finally:
            connection.close()
            return result

    @classmethod
    def delete(cls, tableName, columnName, value):
        connection = Database.connectDb()
        try:
            with connection.cursor() as cursor:
                Query = f"DELETE * FROM `{tableName}` WHERE {columnName}={value}"
                cursor.execute(Query)
                result = cursor.fetchall()
        finally:
            connection.close()
