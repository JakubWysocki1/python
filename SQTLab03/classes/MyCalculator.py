from decimal import Decimal
import math
class MyCalculator():
    def calculate_one(self, operand):
        calculated_value = operand * 100 / math.pi
        ret = Decimal(calculated_value)
        return ret
    def calculate_two(self, operand):
        calculated_value = operand * 100 * math.pi
        ret = Decimal(calculated_value)
        return ret
        
my_cal = MyCalculator()
print('Running definition one', my_cal.calculate_one(1.1))
print('Running definition two', my_cal.calculate_two(3))