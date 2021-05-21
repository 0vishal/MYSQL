'''
@Author: Vishal Salaskar
@Date: 2021-05-20
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-20
@Title : Program to create stored procedures and perform operations on it
'''
import Procedure as sp

def Main():
    """
    Description:
    Function :To get input options to call the required method from class 
    """
    try:
        option = int(input("Enter the procedure to extract 1. All stock prices  2. Show status 3. Drop procedure 4. Single stock price 5. Stocks list   "))
        if option==1:
            price = sp.Procedure()
            price.get_price()
            price.show_prices()
        elif option==2:
            status = sp.Procedure()
            status.show_status()
        elif option==3:
            drop = sp.Procedure()
            drop.drop_procedure()   
        elif option==4:
            selective = sp.Procedure()
            selective.get_stock_price()
            selective.show_stockprice() 
        elif option==5:
            stock_list = sp.Procedure()
            stock_list.stock_list_view()         
        else:
            print("Invalid") 
    except Exception as e:
        print(e,"Enter valid input")
    except (ValueError,KeyboardInterrupt) as e:
        print(" Enter valid input",e)

Main()