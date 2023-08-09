import unittest
from dnf import create_dnf

class Testednf(unittest.TestCase):
    def test_output_1(self):
        truth_table = "a | b | c | (a&b)|(b&c)\n=======================\n0 | 0 | 0 | 0\n0 | 0 | 1 | 0\n0 | 1 | 0 | 0\n0 | 1 | 1 | 1\n1 | 0 | 0 | 0\n1 | 0 | 1 | 0\n1 | 1 | 0 | 1\n1 | 1 | 1 | 1"
        variables = ["a","b","c"]
        correct_result = "(~a&b&c)|(a&b&~c)|(a&b&c)"
        print(create_dnf(truth_table,variables))
        self.assertEqual(create_dnf(truth_table,variables),correct_result)
    
    def test_output_2(self):
        truth_table = "a | b | a>b\n===========\n0 | 0 | 1\n0 | 1 | 1\n1 | 0 | 0\n1 | 1 | 1"
        variables = ["a","b"]
        correct_result = "(~a&~b)|(~a&b)|(a&b)"
        print(create_dnf(truth_table,variables))
        self.assertEqual(create_dnf(truth_table,variables),correct_result)

    def test_output_3(self):
        truth_table = "a | b | a=b\n===========\n0 | 0 | 1\n0 | 1 | 0\n1 | 0 | 0\n1 | 1 | 1"
        variables = ["a","b"]
        correct_result = "(~a&~b)|(a&b)"
        print(create_dnf(truth_table,variables))
        self.assertEqual(create_dnf(truth_table,variables),correct_result)
    
    def test_output_4(self):
        truth_table = "a | b | c | (~a|b)>c\n====================\n0 | 0 | 0 | 0\n0 | 0 | 1 | 1\n0 | 1 | 0 | 0\n0 | 1 | 1 | 1\n1 | 0 | 0 | 1\n1 | 0 | 1 | 1\n1 | 1 | 0 | 0\n1 | 1 | 1 | 1"
        variables = ["a","b","c"]
        correct_result = "(~a&~b&c)|(~a&b&c)|(a&~b&~c)|(a&~b&c)|(a&b&c)"
        print(create_dnf(truth_table,variables))
        self.assertEqual(create_dnf(truth_table,variables),correct_result)
