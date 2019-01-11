import os

while (True):
    f = open("records.txt", "r+")
    n = 1
    book_dict = {}
    for line in f:
        line = line.replace("\n", "")
        line = line.replace("[", "")
        line = line.replace("]", "")
        line = line.replace("'", "")
        line = line.replace("$", "")
        book_dict[n] = line.split(",")
        n += 1
    f.close()

    fp = open("ids.txt", "r")
    i = 1
    std_dict = {}
    for line in fp:
        line = line.replace("\n", "")
        line = line.replace("[", "")
        line = line.replace("]", "")
        line = line.replace("'", "")
        book_dict[n] = line.split(",")
        i += 1
    fp.close()

    def display():
        print "========================== Library Management System ==============================="
        print ""
        print " Book Id. \tTitle of Book \t\t Writer \t\tAvailable  \tAmount"
        print ""

        with open('records.txt', 'r') as f:                  #f_ = open('records.txt', 'r')
            n = 1
            for line in f:
                line = line.replace(",", "\t\t")
                line = line.replace("[", "")
                line = line.replace("]", "")
                line = line.replace("'", "")
                print "   ", n, "\t\t" + line
                n += 1
        print "===================================================================================="

    def borrow():
        #x = 0
        #no_of_book = input("Enter the number of books you want to borrow: ")

        #while(x != no_of_book):
        book_id = int(input("\nEnter the ID No. of the book."))
        if book_id in book_dict:
            borrow_note(book_id)
        else:
            print "Book not Found!!"

    def borrow_note(a):
        name = raw_input("Enter your Name: ")
        borrow_date = raw_input("Date (dd/mm/yyyy): ")
        book_name = book_dict[a][0]
        borrow_cost = int(book_dict[a][3])
        current_quantity = int(book_dict[a][2])
        book_dict[a][2] = current_quantity - 1

            #Store user record
        fp = open ("ids.txt", "w")
        fp.write(str(name) + "," + str(borrow_date) + "," + str(a) + "," + str(borrow_cost) + "\n")
        fp.close()

            #updating the file
        os.remove("records.txt")
        f = open ("records.txt", "w")
        for x, y in book_dict.items():
            f.write(str(y) + "\n")
        f.close()


        print "Name: ",name
        print "Book Name: ",book_name
        print "Total Amount: $",borrow_cost
        print "The book should be returned in 10 days, otherwise additional charge of $10 would be added."


    def return_():
        #x = 0
        #no_of_book = input("Enter the number of books you want to borrow: ")

        #while(x != no_of_book):
        book_id = int(input("\nEnter the ID No. of the book."))
        if book_id in book_dict:
            return_note(book_id)
        else:
            print "Book not Found!!"


    def return_note(a):
        name = raw_input("Enter your Name: ")
        return_date = input("Date (dd/mm/yyyy): ")
        book_name = book_dict[a][0]
        borrow_cost = int(book_dict[a][3])
        current_quantity = int(book_dict[a][2])
        book_dict[a][2] = current_quantity + 1

                #updating the file
        os.remove("records.txt")
        f = open ("records.txt", "w")
        for x, y in book_dict.items():
            f.write(str(y) + "\n")
        f.close()

        print "Name: ",name
        print "Book Name: ",book_name
        print "Thank you for returning the book."


    display()
    #print dict
    print "1. Borrow"
    print "2. Return"
    print "3. Exit"
    choice = input(">>")

    if choice == 1:
        borrow()
    elif choice == 2:
        return_()
    elif choice == 3:
        exit()
