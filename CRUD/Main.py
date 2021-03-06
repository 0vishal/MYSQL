'''
@Author: Vishal Salaskar
@Date: 2021-05-20
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-20
@Title : Program to perform basic crud operations
'''
import CRUD as op

option = int(input("Enter the option : 1: Create 2: Read 3: Update 4: Delete "))

def Main():
    """
		Description
 		Function To insert value in database table stocks data
	"""
    try:
        if option==1:
            create = op.CRUD()
            create.create()
        elif option==2:
            read = op.CRUD()
            read.read()
        elif option==3:
            update = op.CRUD()
            update.update()
        elif option==4:
            delete = op.CRUD()
            delete.delete()    
        else: 
            print("Enter correct option")
    except ValueError as e:
        print(e)         

Main()
