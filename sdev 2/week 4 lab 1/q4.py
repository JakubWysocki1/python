def longest_string(sting_one, string_two):
    if len(sting_one) > len(string_two):
        print("The longer string is :", sting_one)
    else:
        print("The longer string is:", string_two)

string_one = input("Enter the first word: ")
string_two = input("Enter the second word: ")
print()

longest_string(string_one, string_two)