'''
@Author: Vishal Salaskar
@Date: 2021-05-22
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-22
@Title : Program to perform operations on database using built in functions
'''
import Operations as op

def Main():
    """
    Description:
    Function : To get input from user and call the required function
    """
    option = int(input("Enter the option  \n 1.Read Data \n 2. Get Name with Length \n 3. Concatenate Stocks and price \n 4.Get Lower case Name \n 5. Get chars of Name \n 6.Reverse \n 7.Uppercase Name \n 8. Count of traders \n 9. Minimum price stock \n 10. Maximum price stock \n 11. Sum of Stock prices \n 12.Get Date \n 13.Get Time \n 14.Get Day and months details \n 15. Current User \n 16: Current Database \n"))
    try:
        if option==1:
            read = op.Operations()
            read.read()
        elif option==2:
            length = op.Operations()
            length.get_string_length()
        elif option==3:
            concat = op.Operations()
            concat.concatenate_data()        
        elif option==4:
            lower = op.Operations()
            lower.get_lowercase()          
        elif option==5:
            chars = op.Operations()
            chars.get_chars()    
        elif option==6:
            reverse = op.Operations()
            reverse.get_reverse()    
        elif option==7:
            upper = op.Operations()
            upper.get_uppercase()    
        elif option==8:
            count = op.Operations()
            count.get_count() 
        elif option==9:
            min = op.Operations()
            min.get_min()
        elif option==10:
            max = op.Operations()
            max.get_max()
        elif option==11:
            sum = op.Operations()
            sum.get_sum() 
        elif option==12:
            date = op.Operations()
            date.get_date()
        elif option==13:
            time = op.Operations()
            time.get_time() 
        elif option==14:
            day = op.Operations()
            day.get_day()
            day.get_dayname()
            day.get_month()
            day.get_monthname() 
        elif option==15:
            user = op.Operations()
            user.get_currentuser()
        elif option==16:
            name = op.Operations()
            name.get_database()    
        else:
            print("Wrong input")
        
    except (ValueError,KeyboardInterrupt):
        print("Invalid input ")            

Main()        

