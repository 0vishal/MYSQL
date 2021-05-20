'''
@Author: Vishal Salaskar
@Date: 2021-05-20
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-20
@Title : Program to perform basic crud operations
'''

import mysql.connector
from mysql.connector import cursor

class CRUD:

	def __init__(self):
		self.localhost     = "localhost"
		self.username      = "root"
		self.password      = "Root@123"
		self.database_name = "stockmarket" 
		self.__table_name 	 = "stocks_data" 
		self.createConnection()

	def create(self):
		"""
		Description
 		Function To insert value in database table stocks data
		"""

		try:
			print('Enter your name:')
			name = input()
			print('Enter your address:')
			address = input()
		
			print(e)
			cursor = self.db.cursor()

			val = (name, address)
			cursor.execute("INSERT INTO "+self.__table_name+" (stockname, stockprice) VALUES (%s, %s)", val)

			self.db.commit()

			print(cursor.rowcount, "record inserted.")
		except ValueError as e:
			print(e)

	def read(self):
		"""
		Description
 		Function To read the values from table stocks_data
		"""
		

		try:
			cursor = self.db.cursor()

			cursor.execute("SELECT * FROM "+self.__table_name+"")

			myresult = cursor.fetchall()

			for x in myresult:
				print(x)

		except ValueError as e:
			print(e)


	def update(self):
		"""
		Description
 		Function To update value in database table stocks data
		"""

		try:
			print("Enter id")
			id = input()

			print('Edit name:')
			name = input()

			print('Edit price:')
			price = input()
				
			cursor = self.db.cursor()
			val = (name,price,id)

			cursor.execute("update " +self.__table_name+ " set stockname=%s, stockprice=%s where stockid=%s",val)

			self.db.commit()

			print(cursor.rowcount, "record update.")

		except ValueError as e:
			print(e)	

	def delete(self):
		"""
		Description
 		Function To delete value in database table stocks data
		"""

		try:
			print('Search by id to delete:')
			stockid = input()
						
			cursor = self.db.cursor()

			cursor.execute("DELETE FROM "+self.__table_name+" WHERE stockid=%s", (stockid,))

			self.db.commit()

			print(cursor.rowcount, "record deleted")
		except ValueError as e:
			print(e)


	def createConnection(self):
		"""
		Description
 		Function To create connection to the database
		"""

		db = mysql.connector.connect(
		host     = self.localhost,
		user     = self.username,
		passwd   = self.password,
		database = self.database_name
		)
		self.db = db
	
	