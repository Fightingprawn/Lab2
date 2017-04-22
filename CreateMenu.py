"""Description: returns a string that, when printed, will list the options vertically with numbers preceding each option
Precondition: optionList must be a list of strings, menuTitle must be a string
"""
"""
Description: Creates a menu format with the Parameters.
"""

__author__="Ethan Storm"
__date__="February 7, 2017"

def CreateMenu(optionList, menuTitle):
    """
    Description: Creates a menu using the parameters given
    Precondition: optionList must be a list of strings
                  menuTitle must be a string.
    """
    if not type(optionList)==list:
        return None
    
    ct=0
    St=menuTitle+"\n"
    
    for el in optionList:
        ct+=1
        St+="\t"+str(ct)+". "+ el+"\n"
    return St

def getValidChoice(menuString:str, menuTitle:str, numOptions:int):
    """
    Description:
       prints the menuTitle and the menuString and
       continues to print the menuTitle and menuString and ask the user
       to enter a choice until they enter a valid numeric choice
       that is in the proper range.
       Returns an integer.

    PreConditions:
       menuString must be a string that contains the
           numbered options for the choices
       menuTitle must be a string
       numOptions is an integer indicating the number of options for that menu
    """
    
    czech=True
    while czech:
        xList=input("\n"+menuString+"\nPlease enter your choice: ")
        test=True
        try:
            yList=eval(xList)
        except:
            test=False

        if test and type(yList)==int and yList > 0 and yList <=numOptions:
            czech=False

        else:
            print("Invalid choice - try again")

    return yList

def getValidChoices(menuString:str, start:int, end:int):
    """
    Description:
       prints  the menuString and
       continues to print the menuTitle and menuString and ask the user
       to enter a choice until they enter a valid numeric choice
       that is in the proper range.
       Returns an integer.

    PreConditions:
       menuString must be a string that contains the
           numbered options for the choices
       
       dtsrt and end are integers indicating the number of options for that menu
    """
    
    czech=True
    while czech:
        xList=input("\n"+menuString+"\nPlease enter your choice: ")
        test=True
        try:
            yList=eval(xList)
        except:
            test=False

        if test and type(yList)==int and yList>=start and yList <=end:
            czech=False

        else:
            print("Invalid choice - try again")

    return yList

def main():
    x = CreateMenu(["item1","item2"], "Title")
    if x == None:
        return "Not a Valid Menu"
    print(x)      
    choice=input("Enter the number of the opion you wish to use: ")
    return choice


    
if __name__=="__main__":
    main()
