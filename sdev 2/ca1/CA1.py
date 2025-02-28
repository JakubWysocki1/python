"""
Jakub Wysocki - x00164430
CA1
27/02/2020
"""

def menu():
    print("*"*30)
    print("*\t\t HR System \t\t\t *")
    print("\t1 - Add Consultants")
    print("\t2 - Display Emlpoyees")
    print("\t3 - Check departament")
    print("\t4 - Update Pay")
    print("\t5 - Exit")
    print("*" * 30)


def display_employee_info(string_in):
    string_list = string_in.split(":")
    print("\t\t Employee List")
    print("{0:20}{1:10}".format("Employee Code", "Number of years in service"))
    for string in string_list:
        if string[0] == "t":
            years_service = 25
        elif string[0] == "u":
            years_service = 15
        elif string[0] == "c":
            years_service = 1
        else:
            years_service = 0
        print("{0:20}{1:<10}".format(string, years_service))


def valid_dept_name(string_in):
    valid_names = ["IT", "HR", "PR", "it", "hr", "pr"]
    if string_in in valid_names:
        print("The departament entered is valid")
    else:
        print("Invalid Departament name entered")
        print()
        print("Valid departametns")
        print("IT")
        print("HR")
        print("PR")

menu()
choice = int(input("Enter your choice: "))

while choice != 5:
    if choice == 1:
        print("Add Consultants")
        print()
        print()
        consultants_details = []
        for i in range(2):
            cons_name = input("Enter the consultant name: ")
            cons_area_expert = input("Enter the consultant's area of expertise: ")
            cons_hr_rate = input("Enter the consultant's rate per hour: €")
            print()
            single_consultant = [cons_name, cons_area_expert, cons_hr_rate]
            consultants_details.append(single_consultant)

        print(" \t\t Consultant List")
        for one_consultant in consultants_details:
            for details in one_consultant:
                print("{0:20}".format(details), end = "")
            print()



    elif choice == 2:
        print("Display Employees")
        print()
        employees = input("Enter employees :")
        display_employee_info(employees)

    elif choice == 3:
        print("Check Departament")
        print()
        departament_name = input("Please enter a departament name: ")
        valid_dept_name(departament_name)

    elif choice == 4:
        print("Update Pay")
        print()
        employee_details = [["Jack Jones", 1995, 50000.00], ["Mary Smith", 2005, 40000.00]]
        counter = 0
        for employee in employee_details:
            if employee[1] < 2000:
                employee[2] = employee[2] * 1.1
                employee [2] = round(employee[2], 2)
        print("{0:20}{1:20}{2:20}".format("Name", "Start year", "Salary"))
        for employee in employee_details:
            for details in employee:
                print("{0:15}".format(details), end = "")
            print()


    else:
        print("Invalid menu option, please re-enter")


    print()
    menu()
    choice = int(input("Enter your choice: "))
