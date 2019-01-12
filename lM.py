import os
import datetime
import pickle

run = True
while run == True:
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
        std_dict[i] = line.split(",")
        i += 1
    fp.close()

    date_dict = {}


#<-----------------------------------------------------Function defining------------------------------->

    def display():
        print ""
        print ""
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
        std_id = int(input("Enter your Id No: "))

        if std_id in std_dict:
            borrow_date = datetime.date.today()
            book_name = book_dict[a][0]
            borrow_cost = int(book_dict[a][3])
            current_quantity = int(book_dict[a][2])
            book_dict[a][2] = current_quantity - 1

            date_dict[std_id] = borrow_date
            std_dict[std_id][1] = a
            std_dict[std_id][2] = borrow_cost

            save_pickle = open("date_dict.pickle", "w")
            pickle.dump(date_dict, save_pickle)
            save_pickle.close()

            fp = open ("ids.txt", "w")
            for x, y in std_dict.items():
                fp.write(str(y) + "\n")
            fp.close()

                #updating the file
            os.remove("records.txt")
            f = open ("records.txt", "w")
            for x, y in book_dict.items():
                f.write(str(y) + "\n")
            f.close()

            print ""
            print borrow_date                     #print borrow_date
            print ""
            print "Name: ",name
            print "Book Name: ",book_name
            print "Total Amount: $",borrow_cost
            print""
            print "The book should be returned in 10 days, otherwise additional charge of $10 would be added."

        else:
            print "Student Id. Not Found!!"

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
        std_id = int(input("Enter your Id No: "))

        load_pickle = open("date_dict.pickle", "r")
        date_dict = pickle.load(load_pickle)

        if std_id in std_dict:
            return_date = datetime.date.today()
            book_name = book_dict[a][0]
            borrow_cost = int(book_dict[a][3])
            current_quantity = int(book_dict[a][2])
            book_dict[a][2] = current_quantity + 1

            std_dict[std_id][1] = 0
            std_dict[std_id][2] = 0

            fp = open ("ids.txt", "w")
            for x, y in std_dict.items():
                fp.write(str(y) + "\n")
            fp.close()

                    #updating the file
            os.remove("records.txt")
            f = open ("records.txt", "w")
            for x, y in book_dict.items():
                f.write(str(y) + "\n")
            f.close()

            print ""
            print return_date
            print ""
            print "Name: ",name
            print "Book Name: ",book_name
            print ""
            print "Thank you for returning the book."

            late_fee(return_date, date_dict[std_id])

            date_dict[std_id] = 0

            save_pickle = open("date_dict.pickle", "w")
            pickle.dump(date_dict, save_pickle)
            save_pickle.close()


        else:
            print "ID not Found !!"

    def late_fee(a, b):
        diff = a - b
        if diff.days > 10:
            late_fee = diff.days * 2
            print "You are", diff.days,"days late."
            print "So, additional fee = $", late_fee
        else:
            print "Thank You!!"

#<------------------------------------------------------------End of function defining------------------------->
    display()
    try:
        print "1. Borrow"
        print "2. Return"
        print "3. Exit"
        choice = input(">>")

        if choice == 1:
            borrow()
        elif choice == 2:
            return_()
        elif choice == 3:
            run = False
    except:
        print "Enter a Valid Choice !!\n\n"
