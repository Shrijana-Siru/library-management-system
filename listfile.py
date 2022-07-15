#block of code which runs when it is called.
book_name = []
author_name = []
quantity = []
cost = []

#ListSplit fuction is defined using def keyword
def ListSplit():
    global book_name
    global author_name
    global quantity
    global cost
    f = open("books.txt", "r")#this open the text file cointains booklist
    lines = f.readlines()
    #strip() function removes characters from the start
    lines = [x.strip('\n') for x in lines]
    for i in range(len(lines)):
        ind = 0
        for a in lines[i].split(','):
            if ind == 0:
        #adds a single item to the existing list.
                book_name.append(a)
            elif ind == 1:
                author_name.append(a)
            elif ind == 2:
                quantity.append(a)
            elif ind == 3:
                cost.append(a.strip("$"))
            ind += 1# increament a value
