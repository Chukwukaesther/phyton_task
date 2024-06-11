import unittest
from function import len_function


class MyTestCase(unittest.TestCase):
    def test_for_string(self):
        self.assertEqual(len_function("semicolon"),9)

    def test_for_list(self):
        self.assertEqual(len_function([1,2,3,3,4,4,5]),7)

    def test_empty_string(self):
        self.assertEqual(len_function(""),0)#

    def test_string_and_numbers_in_a_list(self):
        self.assertEqual(len_function(["esther",1,2,"badfeez"]), 4)# add assertion here

    def test_string_in_a_list(self):
        self.assertEqual(len_function(["esther","oluchi","chukwuka"]),3)

    def test_string_and_integer_in_a_list(self):
        self.assertEqual(len_function("esther@12"),9)

if __name__ == '__main__':
    unittest.main()
