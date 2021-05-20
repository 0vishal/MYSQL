'''
@Author: Vishal Salaskar
@Date: 2021-05-20
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-20
@Title : Program to perform View and Index operations 
'''

import mysql.connector
from mysql.connector import cursor

class DataQuery:

    def __init__(self):
        self.localhost="localhost"
        self.username="root"
        self.password="Root@123"
        self.database_name="stock_market"
        self.create_connection()

    def read(self):
        """
        Description:
        Function : To read data from table in database 
        """
        try:
            tablename = input("Enter table name to retrive 1> stocks_data 2> traders")
            cursor = self.db.cursor()
            cursor.execute("select * from "+tablename+"")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except ValueError as e:
            print(e)          

    def stock_list_view(self):
        """
        Description:
        Function : To read data from a view created of table column
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT * FROM stocklist")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except ValueError as e:
            print(e)        

    def traders_stock_view(self):
        """
        Description:
        Function : To read data from a view using inner join from table
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT * FROM tradersstocks")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except ValueError as e:
            print(e)        

    def sectors_index(self):
        """
        Description:
        Function : To read a index table column
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT sectors FROM stocks_data")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except ValueError as e:
            print(e)        



    def create_connection(self):
        db = mysql.connector.connect(
            host = self.localhost,
            user = self.username,
            passwd = self.password,
            database = self.database_name
        )
        self.db = db


