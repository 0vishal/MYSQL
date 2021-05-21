'''
@Author: Vishal Salaskar
@Date: 2021-05-20
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-20
@Title : Program to perform View and Index and Join operations 
'''
import DataQuery as dq

def Main():
    """
    Description:
    Function : To get input from user and call the required function
    """
    option = int(input("Enter the option 1. read table 2. stocklist view 3. traders stock list view 4. sectors data index 5. tradersdata 6. traders stock data 7. stock traders type "))
    try:
        if option==1:
            read = dq.DataQuery()
            read.read()
        elif option==2:
            stockview = dq.DataQuery()
            stockview.stock_list_view() 
        elif option==3:
            stocks = dq.DataQuery()
            stocks.traders_stock_view()       
        elif option==4:
            sectors = dq.DataQuery()
            sectors.sectors_index() 
        elif option==5:
            right = dq.DataQuery()
            right.traders_data()
        elif option==6:
            inner = dq.DataQuery()
            inner.traders_stockdata()
        elif option==7:
            left = dq.DataQuery()
            left.stocks_tradertype()    
        else:
            print("Wrong input")
    except ValueError:
        print("Invalid input ")            

Main()        