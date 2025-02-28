"""
Week 4 Lab 1
Jakub Wysocki
20.02.2020
"""
import csv

with open("pima.csv", "r") as infile:
    csv_list = list(csv.reader(infile))

sum_pressure = 0
counter = 0
for row in csv_list:
    if int(row[2]) != 0:
        sum_pressure += int(row[2])
        counter += 1
average = sum_pressure /counter
average = round(average, 2)
print("The average blood pressure is:", average)

for row in csv_list:
    if int(row[2]) == 0:
        row[2] = average

with open("pimaNew.csv", "w", newline = '') as outfile:
    for row in csv_list:
        write = csv.writer(outfile)
        write.writerow(row)














