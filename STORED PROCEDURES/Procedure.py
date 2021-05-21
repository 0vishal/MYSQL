'''
@Author: Vishal Salaskar
@Date: 2021-05-21
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-21
@Title : Program to create stored procedures and perform operations on it
'''
import re
import mysql.connector
from mysql.connector import cursor
from mysql.connector.errors import custom_error_exception

class Procedure:
    pass
    def __init__(self):
        pass
        self.localhost='localhost'
        self.username='root'
        self.password='Root@123'
        self.database='stock_market'
        self.create_connection()

    def stock_list_view(self):
        """
        Description:
        Function : To read data from a view created of table column : To get list of stocks 
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT * FROM stocklist")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except ValueError as e:
            print(e)    

    def get_price(self):
        """
        Description:
        Function :To create a procedure to get column values from table : To get prices of stocks 
        """
        try:
            
            cursor = self.db.cursor()
            cursor.execute("CREATE PROCEDURE price() BEGIN select stockprice from stocks_data; END;")
        except Exception as e:
            print(e)  

    def get_stock_price(self):
        """
        Description:
        Function :To create a procedure with parameters IN and OUT  : To get price of individual stock 
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("CREATE PROCEDURE get_price(IN value varchar(255),OUT stocks varchar(255)) BEGIN SELECT stockprice INTO stocks FROM stocks_data WHERE stockname = value; END;")
        except Exception as e:
            print(e)

    def show_stockprice(self):
        """
        Description:
        Function :To call a  procedure with parameters IN and OUT  : To get price of individual stock 
        """
        try:
            value = input("Enter the stock name  ")
            cursor = self.db.cursor()
            args = [value,0]
            results = cursor.callproc('get_price',args)
            print(results[1])
        except Exception as e:
            print(e)    


    def show_prices(self):
        """
        Description:
        Function :To create a procedure  : To get prices of stocks 
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("CALL price()")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)        

    def show_status(self):
        """
        Description:
        Function :To get status of all procedures created in database 
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SHOW PROCEDURE STATUS where db = 'stock_market';")
            result = cursor.fetchall()

            for record in result:
                print(record)
        except Exception as e:
            print(e)                            

    def drop_procedure(self):
        """
        Description:
        Function :To drop a  procedure created in database
        """
        try:
            value = input("Enter the procedure name to be dropped :  ")
            cursor = self.db.cursor()
            cursor.execute("DROP PROCEDURE "+value+"")
            print("Procedure has been deleted")
        except Exception as e:
            print(e)

    def create_connection(self):
        db = mysql.connector.connect(
            host = self.localhost,
            user = self.username,
            passwd = self.password,
            database = self.database     
        )
        self.db = db 
