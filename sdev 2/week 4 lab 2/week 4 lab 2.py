"""
Jakub Wysocki & Oluwatosin Sojinrin
Week 4 lab 2
21/02/2020
"""

def menu():
    print("*"*30)
    print("*\t\t Calculator +\t\t *")
    print("1 - Add")
    print("2 - Substraction")
    print("3 - Multiplication")
    print("4 - Division ")
    print("5 - Raise to the power")
    print("6 - List of squares")
    print("7 - Encrypt the message")
    print("8 - Upper and lower case")
    print("9 - Exit")
    print("*" * 30)


def addition(input_one, input_two):
    answer = input_one + input_two
    print("The sum of the numbers is:", answer)


def substraction(input_one, input_two):
    answer = input_one - input_two
    print("The difference between the numbers is:", answer)


def multiplication(input_one, input_two):
    answer = input_one * input_two
    print("The product of the numbers is:", answer)


def division(input_one, input_two):
    answer = input_one / input_two
    print(input_one,"goes into", input_two,":", answer, "times")


def raise_to_power(input_one, input_two):
    answer = input_one ** input_two
    print(input_one, "to the power of", input_two, "is:", answer)


def list_of_squares(input_one, input_two):
    answer = []
    for value in range(input_one, input_two + 1):
        answer.append(value ** 2)
    print("List of squares between", input_one, "and", input_two, ":" , answer)


def encryption(message, key):
    encypted_msg = ' '
    for letter in message:
        ascii = ord(letter)
        ascii += key
        if ascii > ord('z'):
            ascii -= 26
        encypted_msg += chr(ascii)
    print("The original message is:", message)
    print("The encrypted message is:", encypted_msg)


def upper_lower(string):
    counter_lower = 0
    counter_upper = 0
    for letter in string:
        if letter.islower():
            counter_lower += 1
        if letter.isupper():
            counter_upper += 1
    print("The number of upper case letters is:", counter_upper)
    print("The number of lower case letters is:", counter_lower)


menu()
choice = int(input("Please enter menu option: "))
print()

while choice != 9:
        if choice == 1:
            input_one = int(input("Enter the first number: "))
            input_two = int(input("Enter the second number:"))
            addition(input_one, input_two)

        elif choice == 2:
            input_one = int(input("Enter the first number: "))
            input_two = int(input("Enter the second number:"))
            substraction(input_one, input_two)

        elif choice == 3:
            input_one = int(input("Enter the first number: "))
            input_two = int(input("Enter the second number:"))
            multiplication(input_one, input_two)

        elif choice == 4:
            input_one = int(input("Enter the first number: "))
            input_two = int(input("Enter the second number:"))
            division(input_one, input_two)

        elif choice == 5:
            input_one = int(input("Enter the number to be raised to the power: "))
            input_two = int(input("Enter the power (greater than 0): "))
            while input_two < 0:
                input_two = int(input("Re-enter the power (greater than 0): "))
            raise_to_power(input_one, input_two)

        elif choice == 6:
            input_one = int(input("Enter the starting number: "))
            input_two = int(input("Enter the end number: "))
            list_of_squares(input_one, input_two)

        elif choice == 7:
            message = input("Enter a message (no spaces and all lowercase): ")
            key = int(input("Enter the encryption key (1 - 26): "))
            while key < 1 or key > 26:
                key = int(input("Re-enter the key (1 - 26): "))
            encryption(message, key)

        elif choice == 8:
            string = input("Enter a sentence: ")
            upper_lower(string)

        else:
            print("Invalid choice. Please re-enter menu option: ")


        menu()
        choice = int(input("Please enter menu option "))

