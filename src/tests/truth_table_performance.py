import pytest

def generate_postfix(num_of_variables):
    postfix = []
    variables = [chr(ord('a') + i) for i in range(num_of_variables)]

    for i in range(num_of_variables):
        postfix.append(variables[i])
        if i > 0:
            postfix.append("+")
    return postfix

@pytest.mark.benchmark
def test_table_time():
    pass