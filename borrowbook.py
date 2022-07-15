#Importing the modules
from listfile import *
from getdatetime import get_time, getdate
import csv 
#borrow_book fuction is defined using def keyword
def borrow_book():
    success = False
    #making loop
    while (True):
        #input first name
        firstName = input("Enter the first name of the borrower: ")
        #it check if borrower name consist alphabate 
        if firstName.isalpha():
            break
        print("please input alphabet from A-Z")
    while (True):
        lastName = input("Enter the last name of the borrower: ")#input last anme
         #it check if borrower name consist alphabate 
        if lastName.isalpha():
            break#it terminate the loop
        print("please input alphabet from A-Z")
        #memo will be created when borrower borrows the books in .txt
    t = "Borrow=" + firstName + ".txt"
    f = open(t, "w+")
    f.write("      LIBRARY MANAGEMENT SYSTEM \n")
    f.write("       Borrowed By: " + firstName + " " + lastName + "\n")
    f.write("    Date:" + getdate() + "    Time:" + get_time() + "\n\n")
    f.write("S.N. \t\t Bookname \t   Authorname \n")

    while not success:
        print("Please select a option below:")
        for i in range(len(author_name)):
            print("Enter", i, "to borrow book", book_name[i])
        try:
            a = int(input())
            #Using try-except handling
            try:
                if int(quantity[a]) > 0:
                    print("Book is available")
                    #when borrower borrow books then quantity of books decreases by 1
                    f = open(t, "a") 
                    f.write("l. \t\t" + book_name[a] + "\t\t " + author_name[a] + "\n")
                    quantity[a] = int(quantity[a]) - 1
                    data = [book_name, author_name, quantity, cost]
                    #It bring same index from multiple iterable objects together as elements of the same tuples
                    abc = list(map(list, zip(*data)))
                    #this open the text file cointains booklist 
                    file = open('books.txt', 'w', newline='')
                    with file:
                    #returns a writer object that converts data into a delimited string
                        writer = csv.writer(file)
                        writer.writerows(abc)
                    #it checks codes when borrower carry more than one book
                    loop = True
                    count = 1
                    while loop:
                        choice = str(input("Do you want to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no."))
                        if choice.upper() == "Y":#if check the condition
                            count = count + 1
                            #message will be print when user select the option
                            print("Please select a option below:")
                            for i in range(len(author_name)):
                                print("Enter", i, "to borrow book", book_name[i])
                            a = int(input())
                            if int(quantity[a]) > 0:
                                print("Book is available")#message will be print when book is available
                                f = open(t, "a")
                                f.write(str(count)+".\t\t"+ book_name[a] + "\t\t " + author_name[a] + "\n")
                                quantity[a] = int(quantity[a]) - 1
                                data = [book_name, author_name, quantity, cost]
                                #It bring same index from multiple iterable objects together as elements of the same tuples
                                abc = list(map(list, zip(*data)))
                                #this open the text file cointains booklist 
                                file = open('books.txt', 'w', newline='')
                                with file:
                                #returns a writer object that converts data into a delimited string
                                    writer = csv.writer(file)
                                    writer.writerows(abc)

                            else:
                                #message will be print when book is unavailable
                                print('Book is not available')
                                loop = False
                                break#it terminate the loop
                            success = False

                        elif choice.upper() == "N":#if check the condition
                            #message will be print when user retuen book 
                            print("Thank you for borrowing books from us.")
                            print("")
                            loop = False
                            success = True
                        else:
                            #message will be print when user input number instead of alphabetic 
                            print("Please choose as instruction.")
                else:
                    #message will be print when book is unavailable
                    print("Book is not available")
                    # borrow_book()
                    success = False
            #Index error occurs when user code is trying to access an index that is invalid
            except IndexError:
                print("")
                #message will be print when user input out of index
                print("Please choose book according to their number.")
        #value error occours when user tried to assign the value to.
        except ValueError:
            print("")
            print("Please choose as suggested.")
#calling borrow_book function 
if __name__ == '__main__':
    borrow_book()
