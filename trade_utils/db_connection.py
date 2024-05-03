import os
import pymysql
import sqlalchemy
import urllib.parse


class MySQLConnector:
    def __init__(self, user_name, pass_word):

        self.host_mysql = '127.0.0.1'
        self.port_mysql = '3306'
        self.database_mysql = 'fnodatabase'

        self.username = urllib.parse.quote_plus(user_name)
        self.password = urllib.parse.quote_plus(pass_word)

    def get_mysql_connection(self):
        try:
            return sqlalchemy.create_engine(
                f'mysql+pymysql://{self.username}:{self.password}@{self.host_mysql}:{self.port_mysql}/{self.database_mysql}')
        except Exception as e:
            print("Something went wrong:", e)

    def get_pymysql_connection(self):
        try:
            return pymysql.connect(host=self.host_mysql,
                                   user=self.username,
                                   password=self.password,
                                   db=self.database_mysql,
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            print("Something went wrong:", e)


if __name__ == '__main__':
    username_mysql = 'your_username'
    password_mysql = 'your_password'
    com = MySQLConnector(username_mysql, password_mysql)
    # print(com.get_mysql_connection())

