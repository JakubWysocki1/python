year_of_birth = int(input("Input your year of birth (1880-2019): "))
while not int(year_of_birth) in range(1880,2019):
    if year_of_birth < 1880:
        print("u old fk")
    elif year_of_birth > 2019:
        print("gucci gang")

    year_of_birth = int(input("Input your year of birth (1880-2019): "))


CURRENT_YEAR = 2019

age_of_person= CURRENT_YEAR - year_of_birth

print("You were born in", year_of_birth, "and will be(are)", age_of_person, "years old")