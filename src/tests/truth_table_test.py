import unittest
from truth_table import evaluate, create_truth_table

class Testevaluate(unittest.TestCase):
    def test_output_1_ff(self):
        postfix = ['a','b','&']
        variable_bool = {'a': 0, 'b': 0}
        result = evaluate(postfix, variable_bool)
        assert result == False

    def test_output_1_ft(self):
        postfix = ['a','b','&']
        variable_bool = {'a': 0, 'b': 1}
        result = evaluate(postfix, variable_bool)
        assert result == False

    def test_output_1_tf(self):
        postfix = ['a','b','&']
        variable_bool = {'a': 1, 'b': 0}
        result = evaluate(postfix, variable_bool)
        assert result == False
 
    def test_output_1_tt(self):
        postfix = ['a','b','&']
        variable_bool = {'a': 1, 'b': 1}
        result = evaluate(postfix, variable_bool)
        assert result == True

#----------------------------------------------------

    def test_output_2_fff(self):
        postfix = ['a', 'b', '|', 'c', '&', 'a', '>']
        variable_bool = {'a': 0, 'b': 0, 'c':0} 
        result = evaluate(postfix, variable_bool)
        assert result == True

    def test_output_2_fft(self):
        postfix = ['a', 'b', '|', 'c', '&', 'a', '>']
        variable_bool = {'a': 0, 'b': 0, 'c':1} 
        result = evaluate(postfix, variable_bool)
        assert result == True

    def test_output_2_ftf(self):
        postfix = ['a', 'b', '|', 'c', '&', 'a', '>']
        variable_bool = {'a': 0, 'b': 1, 'c':0} 
        result = evaluate(postfix, variable_bool)
        assert result == True

    def test_output_2_ftt(self):
        postfix = ['a', 'b', '|', 'c', '&', 'a', '>']
        variable_bool = {'a': 0, 'b': 1, 'c':1} 
        result = evaluate(postfix, variable_bool)
        assert result == False

    def test_output_2_tff(self):
        postfix = ['a', 'b', '|', 'c', '&', 'a', '>']
        variable_bool = {'a': 1, 'b': 0, 'c':0} 
        result = evaluate(postfix, variable_bool)
        assert result == True

    def test_output_2_tft(self):
        postfix = ['a', 'b', '|', 'c', '&', 'a', '>']
        variable_bool = {'a': 1, 'b': 0, 'c':1} 
        result = evaluate(postfix, variable_bool)
        assert result == True

    def test_output_2_ttf(self):
        postfix = ['a', 'b', '|', 'c', '&', 'a', '>']
        variable_bool = {'a': 1, 'b': 1, 'c':0} 
        result = evaluate(postfix, variable_bool)
        assert result == True

    def test_output_2_ttt(self):
        postfix = ['a', 'b', '|', 'c', '&', 'a', '>']
        variable_bool = {'a': 1, 'b': 1, 'c':1} 
        result = evaluate(postfix, variable_bool)
        assert result == True

#----------------------------------------------------

    def test_output_negation_f(self):
        postfix = ['a', '~']
        variable_bool = {'a': 0}
        result = evaluate(postfix, variable_bool)
        assert result == True

    def test_output_negation_t(self):
        postfix = ['a', '~']
        variable_bool = {'a': 1}
        result = evaluate(postfix, variable_bool)
        assert result == False

#----------------------------------------------------

    def test_output_equivalence_ff(self):
        postfix = ['a', 'b', '=']
        variable_bool = {'a': 0, 'b':0}
        result = evaluate(postfix, variable_bool)
        assert result == True

    def test_output_equivalence_ft(self):
        postfix = ['a', 'b', '=']
        variable_bool = {'a': 0, 'b':1}
        result = evaluate(postfix, variable_bool)
        assert result == False

    def test_output_equivalence_tf(self):
        postfix = ['a', 'b', '=']
        variable_bool = {'a': 1, 'b':0}
        result = evaluate(postfix, variable_bool)
        assert result == False

    def test_output_equivalence_tt(self):
        postfix = ['a', 'b', '=']
        variable_bool = {'a': 1, 'b':1}
        result = evaluate(postfix, variable_bool)
        assert result == True


class Testcreate_truth_table(unittest.TestCase):
    def test_output(self):
        pass

if __name__ == '__main__':
    unittest.main()
