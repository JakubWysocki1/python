import random

def ran_number():
    value = random.randint(0,100)
    print("The random value is: ", value)


for i in range(10):
    ran_number()