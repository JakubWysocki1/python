"""
Jakub Wysocki
Week 2 Lab 1
06/02/2020
"""
print()
print("Phone book Application")
print("*"*30)
print("1 - Look Up a Person")
print("2 - Add a Person")
print("3 - Update a Person")
print("4 - Delete a Person")
print("5 - List of Persons")
print("6 - Quit")
print("*"*30)
choice = int(input("Enter your option: " ))
print()

phone_book = {}
while choice != 6:
    if choice == 1:
        if phone_book:
            name = input("Enter the name of the person you want to look up: ")
            print()
            print(name+"\'s", "phone number is", phone_book[name])
        else:
            print()
            print("Phone book is empty")
        print()

    elif choice == 2:
        name = input("Enter the name that you want to add: ")
        while name in phone_book:
            name = input("Name already in phone book, please re-enter: ")
        ph_number = input("Enter the phone number of the person (9 - 12 characters long): ")
        while len(ph_number) < 9 or len(ph_number) > 12:
            ph_number = input("Phone number too long/short please re-enter (9 - 12 characters long): ")
        phone_book[name] = ph_number
        print("Name and number added")
        print()

    elif choice == 3:
        name = input("Enter the name you want to update: ")
        if name in phone_book:
            ph_number = input("Enter the new phone number: ")
            while len(ph_number) < 9 or len(ph_number) > 12:
                ph_number = input("Phone number too long/short please re-enter (9 - 12 characters long): ")
            print()
            if ph_number != phone_book[name]:
                no_confirmation = input("Are you sure you want to update the number (y = yes): ")
                if no_confirmation == "y":
                    phone_book[name] = ph_number
                    print("Number updated")
            else:
                print("Number is already up to date, no need to update it")

        else:
            print("That name doesn't exist try adding it")

    elif choice == 4:
        name = input("Enter the persons name to be deleted: ")
        if name in phone_book:
            del_confirmation = input("Are you sure you want to delete (y = yes): ")
            if del_confirmation == "y":
                del phone_book[name]
                print("The name has been deleted")
        else:
            print("The name is not in the phone book")

    elif choice == 5:
        if phone_book:
            print()
            print("This is the phonebook list:")
            print("\t", phone_book)

        else:
            print()
            print("The phone book is empty")
        print()

    else:
        print("You chose a invalid option, try again")

    print()
    print("Phone book Application")
    print("*"*30)
    print("1 - Look Up a Person")
    print("2 - Add a Person")
    print("3 - Update a Person")
    print("4 - Delete a Person")
    print("5 - List of Persons")
    print("6 - Quit")
    print("*"*30)
    choice = int(input("Enter your option: " ))