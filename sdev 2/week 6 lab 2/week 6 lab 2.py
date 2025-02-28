"""
Jakub Wysocki & Oluwatosin Sojinrin
06/03/2020
Week 6 Lab 2
"""

def menu():
    print("*"*30)
    print("*\t\tDVD Store\t\t\t *")
    print("*"*30)
    print("*\t1) Add Stock\t\t\t *")
    print("*\t2) Stock list\t\t\t *")
    print("*\t3) Rent DVD\t\t\t\t *")
    print("*\t4) Return DVD\t\t\t *")
    print("*\t5) Search\t\t\t\t *")
    print("*\t6) No Stock list\t\t *")
    print("*\t7) Low Stock list\t\t *")
    print("*\t8) Exit\t\t\t\t\t *")
    print("*"*30)


def add(dvd_titles_in, dvd_copies_in, add_titles_in, add_copies_in):
    dvd_titles_in.append(add_titles_in)
    dvd_copies_in.append(add_copies_in)


def display_stock(dvd_titles_in, dvd_copies_in):
    for i, title in enumerate(dvd_titles_in):
        if dvd_copies_in[i] > 1:
            print("{:15} {:10} copies".format(title, dvd_copies_in[i]))
        else:
            print("{:15} {:10} copy".format(title, dvd_copies_in[i]))


def search(dvd_titles_in, dvd_copies_in, rent_title_in):
    in_stock = False
    for i, title in enumerate(dvd_titles_in):
        if rent_title_in == title and dvd_copies_in[i] > 0:
            in_stock = True
    return in_stock


def rent(dvd_titles_in, dvd_copies_in, rent_title_in):
    rented = False
    for i, title in enumerate(dvd_titles_in):
        if rent_title_in == title:
            dvd_copies_in[i] = dvd_copies_in[i]-1
            rented = True
    return rented


def return_dvd(dvd_titles_in, dvd_copies_in, return_title_in):
    returned = False
    for i, title in enumerate(dvd_titles_in):
        if return_title_in == title:
            dvd_copies_in[i] = dvd_copies_in[i] + 1
            returned = True
    return returned


def list_no_stock(dvd_copies_in, dvd_titles_in):
    no_stock = []
    for i, copies in enumerate(dvd_copies_in):
        if copies == 0:
            no_stock.append(dvd_titles_in[i])
    return no_stock


def display_low_stock(dvd_titles_in, dvd_copies_in):
    for i, copies in enumerate(dvd_copies_in):
        if copies < 4:
            print("{:15} {:10} copies".format(dvd_titles_in[i], copies))


DVD_titles = []
DVD_copies =[]

menu()
choice = int(input("Please enter option: "))

while choice != 8:
    if choice == 1:
        add_stock = int(input("Enter the number of DVDs you want to add to the stock: "))
        for i in range(add_stock):
            add_title = input("Enter the title you want to add: ")
            add_copies = int(input("Enter the number of copies: "))
            add(DVD_titles, DVD_copies, add_title, add_copies)
        print("Stock has been added")

    elif choice == 2:
        display_stock(DVD_titles, DVD_copies)

    elif choice == 3:
        rent_dvd = input("Enter the DVD you want to rent: ")
        in_stock = search(DVD_titles, DVD_copies, rent_dvd)
        if in_stock:
            rented = rent(DVD_titles, DVD_copies, rent_dvd)
            if rented:
                print("DVD successfully rented")
            else:
                print("DVD unsuccessfully rented")
        else:
            print("The DVD is not in stock")

    elif choice == 4:
        user_return_dvd = input("Enter the DVD you want to return: ")
        returned = return_dvd(DVD_titles, DVD_copies, user_return_dvd)
        if returned:
            print("The DVD has been returned")
        else:
            print("The DVD hasn't been returned successfully ")

    elif choice == 5:
        search_dvd = input("Enter the DVD you want to find: ")
        i_stock = search(DVD_titles, DVD_copies, search_dvd)
        if i_stock:
            print(search_dvd, "is in stock")
        else:
            print(search_dvd, "isn't in stock")

    elif choice == 6:
        empty_stock = list_no_stock(DVD_titles, DVD_copies)
        if len(empty_stock) > 0:
            print("Titles that are out of stock: ")
            for title in empty_stock:
                print(title)
        else:
            print("All DVDs are available")

    elif choice == 7:
        display_low_stock(DVD_titles, DVD_copies)

    else:
        print("Choice invalid")


    print()
    menu()
    choice = int(input("Please enter option: "))