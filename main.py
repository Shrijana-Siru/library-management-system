#Importing the modules
from returnbook import returnb
from listfile import ListSplit
from borrowbook import borrow_book
#start fuction is defined using def keyword
def start():
#making loop
    while (True):
#designed for the library management system's interface
#menu have four option that perform particular function and execute the code
        print("*******************************************************")
        print("     WELCOME TO THE LIBRARY MANAGEMENT SYSTEM ")
        print("                  KATHMANDU,NEPAL             ")
        print("*******************************************************")
        print("Press 1. To Display the books")
        print("Press 2. To Borrow a books")
        print("Press 3. To return a books")
        print("Press 4. To exit the libarary")
#Using try-except handling 
        try:
            #input
            choose = int(input("Select a choise from 1-4: "))
            #break the line to display
            print()
            if (choose == 1):#if check the condition
                y = open("books.txt", "r")#this open the text file cointains booklist 
                lines = y.read()
                print(lines)
                print()
            elif (choose == 2):
                ListSplit()#a listsplit function is called in class listSplit
                borrow_book()# a borrow_book function is called in class borrow
            elif (choose == 3):
                ListSplit()#a listsplit function is called in class listSplit
                returnb()#a returnb function is called in class return
            elif (choose == 4):
                print("Thank you for using library management system,visit again")
                break#it terminate the loop
            else:
                #when filed is empty this message will be print
                print("Please enter a valid choise from 1-4")
        except:
            print("Please input as suggested")
#calling the start function
start()
