#Importing the modules
from listfile import *
from getdatetime import get_time, getdate
#returnb fuction is defined using def keyword
def returnb():
    name = input("Enter name of borrower: ")#input first name
    a = "Borrow=" + name + ".txt"
    #Using try-except handling
    try:
        f = open(a, "r")
        lines = f.readlines()
        #strip() function removes characters from the start
        lines = [a.strip("$") for a in lines]
        f = open(a, "r")
        data = f.read()
        print(data)
    except:
        print("The borrower name is incorrect")#memo will be created when borrower name is incorrect
        returnb()

    b = "Return=" + name + ".txt"
    #function opens a file and returns it as a file  'b' and over write it
    f = open(b, "w+") 
    f.write("        LIBRARY MANAGEMENT SYSTEM \n")
    f.write("        Return By: " + name + "  \n")
    f.write("     Date: " + getdate() + "  Time:" + get_time() + "\n\n")
    f.write("S.N.\t\tBookname\t\tCost\n")
    #insitlized total cost
    total = 0.0
    for i in range(10):
        if book_name[i] in data:
            f = open(b, "a") 
            f.write(str(i + 1) + "\t\t" + book_name[i] + "\t\t$" + cost[i] + "\n")
            quantity[i] = int(quantity[i]) + 1
            total += float(cost[i])
            #memo will be printed  when borrower return book after expired
            print("\t\t\t\t\t\t\t" +"Total :$"+ str(total))
            print("Is the book return date expired?")
            
            #print()
    stat = input("Press Y for Yes And N for No: ")            
    if stat.upper() == "Y":                
    #memo will be printed  when borrower return late and print delay amount
        print("By how many days was the book returned late?")                
        day = int(input())
        #if retuen date is expire then it will cost twice 
        delayamount = 2 * day
        f = open(b, "a")
        f.write("\t\t\t\tFine: $" + str(delayamount) + "\n")
        total = total + delayamount

                
    print("Final Cost: " + "$" + str(total))
    f = open(b, "a")
    f.write("\t\t\t\tTotal Cost: $" + str(total))
        
    f = open("books.txt", "w+")#this open the text file cointains booklist
    for i in range(10):
        f.write(book_name[i] + "," + author_name[i] + "," + str(quantity[i]) + "," + "$" + cost[i] + "\n")


