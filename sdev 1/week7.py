"""
Jakub Wysocki
Week 7 Lab
08/11/2019
"""

#Question 1
counter = 50
total = 0

while counter <= 100:
    total += counter
    counter += 1

print("The total of numbers between 50 and including 100 is", total)

total = 0

for number in range(50,101):
    total += number

print("\nThe total of numbers between 50 and including 100 is", total)


#Question 2
counter = 0
total = 0

for counter in range(5):
    number = float(input("\nInput a floating point number:"))
    total += number
    print("The total is", total)


average = total/5
print("\nThe average is", average)


#Question 3
counter = 0
total_odd = 0
total_even = 0

for counter in range(1,21):
    if counter % 2 != 0:
        total_odd += counter

    else:
        total_even += counter


print("\n\nthe total of even numbers between 1 and 21 is", total_even)
print("\nthe total of odd numbers between 1 and 21 is", total_odd)


#Question 4
YEN_PER_EURO = float(input("\n\nEnter the conversion rate for yen per euro:"))

euro = float(input("Enter the amount of euro to be converted (0 to exit program):"))

while euro != 0:
    euro_to_yen = euro * YEN_PER_EURO
    print("€", euro, "in yen is ¥", euro_to_yen, )
    euro = float(input("\nEnter the amount of euro to be converted (0 to exit program):"))


#Question 5
sentence = input("\n\nInput a sentence including commas: ")

comma_count = 0
counter = 0

while counter < len(sentence):
    if sentence[counter] == ",":
        comma_count += 1
    counter += 1

print("\nThe number of commas in the sentence is:", comma_count)
print("the lenght of the sting is:", len(sentence))

#Question 6
start_no = int(input("\n\nPlease input a starting number: "))
end_no = int(input("Please input a end number: "))
step_no = int(input("Please input the steps you want to go up in: "))

sum = 0

for counter in range(start_no, end_no, step_no):
    sum += counter
    print("Counter =",counter, "Sum =", sum)

#Question 7
year = int(input("\n\nPlease input a year: "))

if year % 4 == 0 and year % 100 == 0:
    print("The year is not a leap year ")

else:
    print("\nThe year is a leap year")







