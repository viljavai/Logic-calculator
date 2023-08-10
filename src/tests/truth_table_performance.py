import pytest
from create_table import create_truth_table

def generate_postfix(num_of_variables):
    postfix = []
    variables = [chr(ord('a') + i) for i in range(num_of_variables)]

    for i in range(num_of_variables):
        postfix.append(variables[i])
        if i > 0:
            postfix.append("+")
    return postfix

def generate_expression(num_of_variables):
    variables = [chr(ord('a') + i) for i in range(num_of_variables)]
    expression = '+'.join(variables)
    print(expression)

@pytest.mark.parametrize("num_of_variables", list(range(1, 21)))
def test_table_time(benchmark, num_of_variables):
    postfix = generate_postfix(num_of_variables)
    expression = generate_expression(num_of_variables)
    result = benchmark(create_truth_table, postfix, expression)
    print(result)
