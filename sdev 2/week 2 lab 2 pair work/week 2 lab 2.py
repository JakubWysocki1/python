"""
Jakub Wysocki
07/02/2020
Week 2 Lab 2
"""
from statistics import mean

grade = [[10.5, 12.0, 14.5, 16.75, 18.0], [20.5, 22.25, 24.0, 26.25, 28.0], [34.0, 36.5, 38.0, 40.35, 43.0], [50.0, 60.0, 70.0, 80.0, 99.99]]



mean3 = mean(grade[2])
print("The avarage for grade 3 is: ", mean3)
print()


for i, row in enumerate(grade):
    avg = mean(row)
    print("The avarage for grade", (i+1), "is", avg)
    maximum = max(row)
    minimum = min(row)
    difference = maximum - minimum
    print("The difference between the highest", maximum,"and lowest", minimum, "step is:", round(difference, 2))
    print()


print("{0:^44}".format("Payscale Table"))
print("{0:10}".format("Step 1")+"{0:10}".format("Step 2")+"{0:10}".format("Step 3")+"{0:10}".format("Step 4")+"{0:10}".format("Step 5"))
print("_"*46)

for i, row in enumerate(grade):
    print("Grade", str(i+1), ":", end ="")
    for col in row:
        print("{0:<10}".format(col), end="")
    print()

increase  = 1.5

for row in range(len(grade)):
    for col in range(len(grade[0])):
        grade[row][col] += increase

print(grade)


