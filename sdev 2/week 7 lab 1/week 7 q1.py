"""
Jakub Wysocki
Week 7 q1
12/03/2020
"""

class DogCare:
    DOG_PERCENTAGE_FOOD = 2.5
    DOG_AGE_CHART = [[15, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80],
                     [15, 24, 28, 32, 36, 42, 47, 51, 56, 60, 65, 69, 74, 78, 83, 87],
                     [15, 24, 28, 32, 36, 45, 50, 55, 61, 66, 72, 77, 82, 88, 93, 120]]


    @staticmethod
    def dog_food(dog_lb):
        food_required = DogCare.DOG_PERCENTAGE_FOOD * dog_lb
        return food_required


    @staticmethod
    def dog_age(dog_age_in_human_years, dog_lb):
            if dog_lb <= 20:
                row = DogCare.DOG_AGE_CHART[0]

            elif dog_lb > 20 and dog_lb <= 50:
                row = DogCare.DOG_AGE_CHART[1]

            else:
                row = DogCare.DOG_AGE_CHART[2]

            for i, age in enumerate(row):
                if i == (dog_age_in_human_years - 1):
                    human_years = age

            return human_years


    @staticmethod
    def dog_exercise(dog_age_in_human_years, dog_lb):
        age = DogCare.dog_age(dog_age_in_human_years, dog_lb)
        if  age < 15:
            exercise = 15
        elif age >= 15 and age <= 55:
            exercise = 75
        else:
            exercise = 30

        return exercise

dog_AGE = int(input("Enter the dogs age: "))
weight = float(input("Enter the weight in lb: "))

print("The age of your dog in human years is:", DogCare.dog_age(dog_AGE, weight))
print("The required food is:", DogCare.dog_food(weight))
print("The required exercise is:", DogCare.dog_exercise(dog_AGE, weight), "mins")