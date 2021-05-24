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
        """
        Description:
        Function : To get the string length of string values
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT tradername, CHAR_LENGTH(tradername) AS LengthOfName FROM traders")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e) 

    def concatenate_data(self):
        """
        Description:
        Function : To get the concatenation of columns from tables in database
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT sectors, CONCAT(stockname,stockprice) AS data FROM stocks_data;")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)

    def get_lowercase(self):
        """
        Description:
        Function : To get the lower case of the string in column in databases
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT LCASE(tradername) AS Lowercasename FROM traders;")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)  

    def get_chars(self):
        """
        Description:
        Function : To get specific characters from the string in column from table
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT LEFT(tradername, 3) AS nicekname FROM traders;")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)

    def get_reverse(self):
        """
        Description:
        Function : To get the reverse the string of a column 
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT REVERSE(tradername) FROM traders;")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e) 

    def get_uppercase(self):
        """
        Description:
        Function : To get the uppper case of the string in column
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT UPPER(tradername) AS UppercaseName FROM traders;")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e) 

    def get_count(self):
        """
        Description:
        Function : To get the count of number of records in a column
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT COUNT(tradername) AS numberoftraders FROM traders")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)   

    def get_max(self):
        """
        Description:
        Function : To get the maximum value from the number of records in a given column
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT MAX(stockprice) AS LargestPrice FROM stocks_data")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e)  

    def get_min(self):
        """
        Description:
        Function : To get the minimum from number of records in a column
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT MIN(stockprice) AS Smallestprice FROM stocks_data")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e) 

    def get_sum(self):
        """
        Description:
        Function : To get the sum of values in a columns
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT SUM(stockprice) AS Sumprice FROM stocks_data")
            result = cursor.fetchall()

            for x in result:
                print(x)
        except Exception as e:
            print(e) 

    def get_date(self):
        """
        Description:
        Function : To get the current date
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT CURDATE();")
            result = cursor.fetchall()
            print(result)

        except Exception as e:
            print(e) 

    def get_time(self):
        """
        Description:
        Function : To get the current time 
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT CURTIME();")
            result = cursor.fetchall()
            print(result)

        except Exception as e:
            print(e)             
    
    def get_day(self):
        """
        Description:
        Function : To get the current day 
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT DAY(CURDATE());")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)


    def get_dayname(self):
        """
        Description:
        Function : To get the current day name
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT DAYNAME(CURDATE());")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)  

    def get_month(self):
        """
        Description:
        Function : To get the current month 
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT MONTH(CURDATE());")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)

    def get_monthname(self):
        """
        Description:
        Function : To get the current month name
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT MONTHNAME(CURDATE());")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)                                                                               


    def get_currentuser(self):
        """
        Description:
        Function : To get the current user 
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT CURRENT_USER();")
            result = cursor.fetchall()
            for x in result:
                print(x)

        except Exception as e:
            print(e)    

    def get_database(self):
        """
        Description:
        Function : To get the database name
        """
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
    

