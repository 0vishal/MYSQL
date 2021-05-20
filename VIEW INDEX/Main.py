import DataQuery as dq

def Main():
    option = int(input("Enter the option 1. read table 2. stocklist view 3. traders stock list view 4. sectors data index"))
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
        else:
            print("Wrong input")
    except ValueError as e:
        print(e)            

Main()        