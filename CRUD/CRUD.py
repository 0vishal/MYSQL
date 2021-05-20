import mysql.connector
from mysql.connector import cursor

class CRUD:

	def __init__(self):
		self.localhost     = "localhost"
		self.username      = "root"
		self.password      = "Root@123"
		self.database_name = "stockmarket" 
		self.table_name 	 = "stocks_data" 
		self.createConnection()

	def create(self):
		print('Enter your stockname:')
		name = input()
		print('Enter your price:')
		address = input()

		cursor = self.db.cursor()

		val = (name, address)
		cursor.execute("INSERT INTO "+self.table_name+" (stockname, stockprice) VALUES (%s, %s)", val)

		self.db.commit()

		print(cursor.rowcount, "record inserted.")

	def read(self):
		cursor = self.db.cursor()

		cursor.execute("SELECT * FROM "+self.table_name+"")

		myresult = cursor.fetchall()

		for x in myresult:
		  print(x)

	def update(self):
		print('Search by id:')
		id = input()

		print('Edit name:')
		name = input()


		print('Edit price:')
		price = input()

	
		cursor = self.db.cursor()
		val = (name,price,id)

		cursor.execute("update " +self.table_name+ " set stockname=%s, stockprice=%s where stockid=%s",val)

		self.db.commit()

		print(cursor.rowcount, "record update.")

	def delete(self):
		print('Search by id to delete:')
		stockid = input()
		
		cursor = self.db.cursor()

		cursor.execute("DELETE FROM "+self.table_name+" WHERE stockid=%s", (stockid,))

		self.db.commit()

		print(cursor.rowcount, "record deleted")


	def createConnection(self):
		db = mysql.connector.connect(
		  host     = self.localhost,
		  user     = self.username,
		  passwd   = self.password,
		  database = self.database_name
		)

		self.db = db