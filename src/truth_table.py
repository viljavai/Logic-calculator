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
                #this is an equivalent form that can be checked with a truth table
                #for example if you don't believe me
                result = (not oper1) or oper2
            elif token == '=':
                result = oper1 == oper2

            stack.append(result)

    # Now with all operators handled, the result is at the bottom of the stack
    return stack[0]
