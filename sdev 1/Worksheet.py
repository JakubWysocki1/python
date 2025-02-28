from statistics import mean

my_list = []
total = 0


for student in range(2):
    marks = []
    for test in range(2):
        test_mark = int(input("Enter the "+str(test+1)+" test mark for student no."+str(student+1)+": "))
        while 100 < test_mark or test_mark < 0:
            test_mark = int(input("Re-Enter the " + str(test + 1) + " test mark for student no." + str(student + 1)+": "))
        marks.append(test_mark)

    my_list.append(marks)
    print()

avg_total = 0
total_avg_total = 0

for avg in my_list:
    avg_total += mean(avg)
total_avg_total = avg_total/len(my_list)
print("The total avarage is",total_avg_total)
print()

counter = 0

for i, row in enumerate(my_list):
    print("Student", str(i+1) )
    print("Avarage mark is", mean(row))
    difference = mean(row) - total_avg_total
    print("The difference from overall avarage marks is:", round(difference, 2), "mark(s)")
    if mean(row) >= total_avg_total:
        print("Good job you're not below avarage")
        counter += 1
    print()

print("The number of students whose average is equal to or greater than the overall average is:", counter)
print()



















