'''
@Author: Vishal Salaskar
@Date: 2021-05-20
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-20
@Title : Program to perform import export operations 
'''

import mysql.connector
from mysql.connector import cursor 
import pandas as pd

class Import:

    def __init__(self):
        self.localhost="localhost"
        self.username="root"
        self.password="Root@123"
        self.database="employees"
        self.create_connection()

    

    def import_csv(self):
        """
        Description:
        function :  Define to import table from csv file
        """
        try:
            data = pd.read_csv('username.csv')
            data.head()
            if self.db.is_connected():
                cursor = self.db.cursor()
                cursor.execute("CREATE TABLE employee_data ( Username varchar(255), Identifier varchar(255), Firstname varchar(255), Lastname varchar(255)")
                for i,row in data.iterrows():
                    sql = "INSERT INTO employee_data VALUES (%s,%s,%s,%s)"
                    cursor = self.db.cursor()
                    cursor.execute(sql, tuple(row))
                self.db.commit()
        except Exception as error:
            print(error)    

    def get_import_data(self):
        """
        Description:
        function : To read the data from imported table  
        """
        try:
            cursor = self.db.cursor()
            sql = "SELECT * FROM employee_data"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                print(i)
        except Exception as e:
            print(e)

    def create_connection(self):
        db = mysql.connector.connect(
            host = self.localhost,
            user = self.username,
            passwd = self.password,
            database= self.database
        )
        self.db = db                