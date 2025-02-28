import unittest
from classes.MyCalculator import MyCalculator
from decimal import Decimal
import math

class test_MyCalculator(unittest.TestCase):
    def setUp(self):
        self.my_test_cal = MyCalculator()

    def test_calculate_one(self):
        test_data = 1.1
        expected_value = Decimal(test_data * 100 / math.pi)
        actual_value = self.my_test_cal.calculate_one(test_data)
        self.assertEqual(expected_value, actual_value)

    def test_calculate_two(self):
        test_data = 3
        expected_value = Decimal(test_data * 100 * math.pi)
        actual_value = self.my_test_cal.calculate_two(test_data)
        self.assertEqual(expected_value, actual_value)
        