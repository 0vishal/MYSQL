'''
@Author: Vishal Salaskar
@Date: 2021-05-20
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-20
@Title : Program to perform import export operations 
'''
import Import as ie
import Export as ex

def Main():
    """
    Description:
    Function : To get input from user and call the required function
    """
    option = int(input("Enter the option 1.Import Data  2. Export data "))
    try:
        if option==1:
            import_data = ie.Import()
            import_data.import_csv()
            #import_data.get_import_data()
        elif option==2:
            export_data = ex.Export()
            export_data.export_data()
    except (ValueError,KeyboardInterrupt) as e:
        print(e)     

Main()