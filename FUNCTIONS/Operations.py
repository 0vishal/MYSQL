'''
@Author: Vishal Salaskar
@Date: 2021-05-22
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-22
@Title : Program to perform operations on database using built in functions
'''

import mysql.connector
from mysql.connector import cursor

class Operations:

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

    def get_string_length(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT tradername, CHAR_LENGTH(tradername) AS LengthOfName FROM traders")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e) 

    def concatenate_data(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT sectors, CONCAT(stockname,stockprice) AS data FROM stocks_data;")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)

    def get_lowercase(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT LCASE(tradername) AS Lowercasename FROM traders;")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)  

    def get_chars(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT LEFT(tradername, 3) AS nicekname FROM traders;")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)

    def get_reverse(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT REVERSE(tradername) FROM traders;")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e) 

    def get_uppercase(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT UPPER(tradername) AS UppercaseName FROM traders;")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e) 

    def get_count(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT COUNT(tradername) AS numberoftraders FROM traders")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)   

    def get_max(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT MAX(stockprice) AS LargestPrice FROM stocks_data")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)  

    def get_min(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT MIN(stockprice) AS Smallestprice FROM stocks_data")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e) 

    def get_sum(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT SUM(stockprice) AS Sumprice FROM stocks_data")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e) 

    def get_date(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT CURDATE();")
            result = cursor.fetchall()
            print(result)

        except Exception as e:
            print(e) 

    def get_time(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT CURTIME();")
            result = cursor.fetchall()
            print(result)

        except Exception as e:
            print(e)             
    
    def get_day(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT DAY(CURDATE());")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)


    def get_dayname(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT DAYNAME(CURDATE());")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)  

    def get_month(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT MONTH(CURDATE());")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)

    def get_monthname(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT MONTHNAME(CURDATE());")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)                                                                               


    def get_currentuser(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT CURRENT_USER();")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)    

    def get_database(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT DATABASE();")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)                                                                                       

    def create_connection(self):
        db = mysql.connector.connect(
            host = self.localhost,
            user = self.username,
            passwd = self.password,
            database = self.database_name
        )
        self.db = db
    

