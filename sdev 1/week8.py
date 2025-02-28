"""
Jakub Wysocki
Week 8 Lab
15/11/2019
"""
import datetime

now = datetime.datetime.now()

CARD_COST = 4.00
COST_CHAR = 0.50

sales_counter = 0
return_counter = 0
total = 0
len_message_counter = 0
return_cost = 0

print("*****************************")
print("*\t\tXmas Card Shop \t\t*")
print("*****************************")
print("* 1) Sale \t\t\t\t\t*")
print("* 2) Return \t\t\t\t*")
print("* 3) Run Report \t\t\t*")
print("* 4) Exit \t\t\t\t\t*")
print("*****************************")
user_choice = int(input("Please select menu option: "))
print()

while user_choice != 4:
    if user_choice == 1:
        print("*****************************")
        print("*\tXmas Card Shop - Sale \t*")
        print("*****************************")
        personal_message = input("Please enter your personal message: ")
        len_message = len(personal_message)

        while len_message > 100:
            print("The personal message cannot exceed 100 characters try again ")
            personal_message = input("Please enter your personal message: ")

        sale_total = CARD_COST + (len_message * COST_CHAR)
        character_cost = len_message * COST_CHAR

        sales_counter += 1
        total += sale_total
        len_message_counter += len_message

        print("Number of characters printed:", len_message)
        print("Cost of characters printed: €", character_cost )
        print("Sale total:\t€", sale_total)
        print("Sale complete:", now.strftime("%d/%m/%Y"), "at", now.strftime("%H:%M"))
        print()



    elif user_choice == 2:
        print("*****************************")
        print("*\tXmas Card Shop - Return\t*")
        print("*****************************")
        card_return = float(input("Please enter the cost of the card to be returned: €"))
        return_counter += 1
        return_cost += card_return
        print()


    elif user_choice == 3:
        if sales_counter > 0:
            avarage_no_char = len_message_counter / sales_counter
            avarage_cost_card = total / sales_counter
        else:
            avarage_no_char = 0
            avarage_cost_card = 0
        print("*****************************")
        print("*\tXmas Card Shop - Report *")
        print("*****************************")
        print("Total sales\t: €", total)
        print("Number of sales\t:",   sales_counter)
        print("Average number of characters printed:", avarage_no_char)
        print("Average cost of a card: €", avarage_cost_card)
        print("Number of returns:", return_counter)
        print("Cost of return", return_cost)
        print()

    else:
        print("Invalid option. Please re- select menu option")
        print()


    print("*****************************")
    print("*\t\tXmas Card Shop \t\t*")
    print("*****************************")
    print("* 1) Sale \t\t\t\t\t*")
    print("* 2) Return \t\t\t\t*")
    print("* 3) Run Report \t\t\t*")
    print("* 4) Exit \t\t\t\t\t*")
    print("*****************************")
    user_choice = int(input("Please select menu option: "))









