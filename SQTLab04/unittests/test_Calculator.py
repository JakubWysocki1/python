

from classes.Calculator import Calculator

import math

from decimal import Decimal


class test_Calculator(unittest.TestCase):
    my_test_obj = Calculator()

    def setUp(self):
        self.my_test_obj = Calculator()        

    def tearDown(self):
        del self.my_test_obj

    def test_alternative_calculate(self):
        my_test_obj = Calculator()
        param1 = 2.2
        expected_result = Decimal(param1 * 100/ math.pi)

        actual_result = self.my_test_obj.alternative_calculate(param1)

        self.assertEqual(actual_result, expected_result)


    def test_is_special_number_numLessThan0_notValidNum(self):
        my_test_obj = Calculator()
        param1 = -1
        expected_result = str(param1) + " is not a valid number."

        actual_result = self.my_test_obj.is_special_number( param1 )

        self.assertEqual(actual_result, expected_result)

    
    def 