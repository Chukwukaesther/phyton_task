import unittest
from assignment_One import random_number, length_in_list, even_numbers


class MyTestCase(unittest.TestCase):
    def test_that_my_random_function_is_working(self):
        self.assertEqual(random_number(1,50), [16, 38, 35, 9, 24, 39, 31, 41, 38, 5] )


    def test_that_my_length_function_is_working(self):
        names = ["Glory", "Chi-Chi", "Melody", "Fantasy"]
        self.assertEqual(length_in_list(names), 4)
        # add assertion here


    def test_that_my_even_function_is_working(self):
        digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(even_numbers(digit), 30)


if __name__ == '__main__':
    unittest.main()
