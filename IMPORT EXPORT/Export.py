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
import csv

class Export:

    def __init__(self):
        self.localhost="localhost"
        self.username="root"
        self.password="Root@123"
        self.database="stock_market"
        self.create_connection()

    def export_data(self):
        """
        Description:
        function :  Define to export data from database to csv file
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("select * from stocks_data")
            rows = cursor.fetchall()
            file = open('output.csv', 'w')
            opfile =  csv.writer(file)
            opfile.writerows(rows)
            file.close()
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