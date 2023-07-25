import unittest
from shunting_yard import shunting_yard

class Testshunting_yard(unittest.TestCase):
    def test_output_1(self):
        expression = "~(A&B)|A"
        correct_postfix = ['A', 'B', '&', '~', 'A', '|']
        self.assertEqual(shunting_yard(expression), correct_postfix)

    def test_output_2(self):
        expression = "((A|B)&(C|A))|(A|D)"
        correct_postfix = ['A', 'B', '|', 'C', 'A', '|', '&', 'A', 'D', '|', '|']
        self.assertEqual(shunting_yard(expression), correct_postfix)

    def test_output_3(self):
        expression = "A"
        correct_postfix = ["A"]
        self.assertEqual(shunting_yard(expression), correct_postfix)

    def test_output_4(self):
        expression = "A&A"
        correct_postfix = ["A","A","&"]
        self.assertEqual(shunting_yard(expression), correct_postfix)

    def test_mismatched_brackets_too_many_right(self):
        try:
            wrong_expression = "(A))"
            result = shunting_yard(wrong_expression)
            assert False, "Expected a SyntaxError, no error"
        except SyntaxError as error:
            assert str(error) == "Expression contains mismatched brackets, please check your input!", f"Error: {str(error)}"

    def test_mismatched_brackets_too_many_left(self):
        try:
            wrong_expression = "((A)"
            result = shunting_yard(wrong_expression)
            assert False, "Expected a SyntaxError, no error"
        except SyntaxError as error:
            assert str(error) == "Expression contains mismatched brackets, please check your input!", f"Error: {str(error)}"

    def test_output_empty(self):
        try:
            wrong_expression = ""
            result = shunting_yard(wrong_expression)
            assert False, "Expected a SyntaxError, no error"
        except SyntaxError as error:
            assert str(error) == "Empty input!", f"Error: {str(error)}"

    def test_output_no_variables(self):
        try:
            wrong_expression = "&|>"
            result = shunting_yard(wrong_expression)
            assert False, "Expected a SyntaxError, no error"
        except SyntaxError as error:
            assert str(error) == "Expression does not contain any variables, please check your input!", f"Error: {str(error)}"

    def test_output_invalid_character(self):
        try:
            wrong_expression = "a?b"
            result = shunting_yard(wrong_expression)
            assert False, "Expected a SyntaxError, no error"
        except SyntaxError as error:
            assert str(error) == "Expression contains invalid character: ?, please check your input!", f"Error: {str(error)}"


if __name__ == '__main__':
    unittest.main()