import unittest
from classes.Grade import Grade

class test_grade(unittest.TestCase):
    param_list = [
        (45,40,"Fail"),
        (38,97,"Component Fail")
    ]

    def test_calculate_grade_category(self):
        for exam_result, ca_result, expected_grade in self.param_list:
            with self.subTest():
                my_test_object = Grade ( exam_result, ca_result)
                print("\n", exam_result, ca_result, expected_grade, "\n")
                actual_result = my_test_object.calculate_grade_category()

                self.assertEquals(actual_result, expected_grade)