import itertools
from truth_table import evaluate

def create_truth_table(postfix, expression):
    """Function that creates the truth table

    Args: 
        postfix(list): The original expression in postfix notation
        expression(string): The original expression

    Returns:
        table: The final truth table
        variables(set): A set of variables used in the expression

    """
    # Each variable should appear only once -> set
    variables = set()
    variable_bool = {}

    for token in postfix:
        if token.isalpha():
            variables.add(token)
    # We sort the variables to get a consistent set each time
    variables = sorted(variables)

    head = " | ".join(variables) + f" | {expression}"
    table_lines = [head, "=" * len(head)]

    for combination in itertools.product([0, 1], repeat=len(variables)):
        for i, variable in enumerate(variables):
            variable_bool[variable] = combination[i]
        result = evaluate(postfix, variable_bool)
        row = " | ".join(str(int(combination[i])) for i in range(len(variables))) + f" | {int(result)}"
        table_lines.append(row)
    table = "\n".join(table_lines)

    return table,variables
