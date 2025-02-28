import math
from decimal import *

class Calculator():

     """
     A special number is any number that is
      - is between 0 and 100 inclusive and
      - divisible by two and
      - divisible by five.
      @param number
      @return message (that displays if the number is a special number)
     """
     def is_special_number(self, num_in):
        # Verify the number is within the valid range.
        if num_in < 0 or num_in > 100:
            message = " is not a valid number."
        else:
            # Determine if the number is a special number.
            if num_in % 2 != 0:
                message = " is not an even number."
            elif num_in % 5 != 0:
                message = " is not divisible by five."
            else:
                message = " is a special number"

        #Remember this will return your number plus the message!
        return str(num_in) + message

     """ 
     This method does a strange/alternative calculation
     * @param operand
     * @return calculated value as a Decimal 
     """
     def alternative_calculate(self, operand):
         calculated_value = operand * 100 / math.pi
         return Decimal(calculated_value)


if __name__ == '__main__':
    print("******                      *******    ")
    print("****** Running calculator   *******    ")
    calc = Calculator()

    num1 = int(input("Please enter a number to check if it is special: " ))
    print("-> ", calc.is_special_number(num1))

    num2 = int(input("Please enter a number to run an alternative calculation on it: " ))
    print("-> ", round(calc.alternative_calculate(num2),4))
