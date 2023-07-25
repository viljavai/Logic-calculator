import itertools

""" First we create an empty table in create_truth_table() and then
do the actual logical steps in evaluate(). 
variable_bool contains all combinations on boolean values 
for our variables."""

def evaluate(postfix, variable_bool):
    stack = []
    operators = {'~', '&', '|', '>', '='}

    for token in postfix:
        if token.isalpha():
            stack.append(variable_bool[token])

        elif token == '~':
            oper = stack.pop()
            result = not oper
            stack.append(result)

        elif token in operators and token != '~':
            oper2 = stack.pop()
            oper1 = stack.pop()

            if token == '&':
                result = oper1 and oper2
            elif token == '|':
                result = oper1 or oper2
            elif token == '>':
                """ this is an equivalent form that can be checked with a truth table
                for example if you don't believe me """
                result = (not oper1) or oper2
            elif token == '=':
                result = oper1 == oper2

            stack.append(result)

    # Now with all operators handled, the result is at the bottom of the stack
    return stack[0]


def create_truth_table(postfix, expression):
    # Each variable should appear only once -> set
    variables = set()
    variable_bool = {}

    for token in postfix:
        if token.isalpha():
            variables.add(token)
    # We sort the variables to get a consistent set each time
    variables = sorted(variables)

    head = " | ".join(variables) + f" | {expression}"
    print(head)
    print("="*len(head))

    for comb in itertools.product([0, 1], repeat=len(variables)):
        for i,variable in enumerate(variables):
            variable_bool[variable] = comb[i]

        result = evaluate(postfix,variable_bool)

        row = " | ".join(str(int(comb[i])) for i in range(len(variables)))+f" | {int(result)}"
        print(row)
