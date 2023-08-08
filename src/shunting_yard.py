#Takes expression and parses into postfix

def shunting_yard(expression):
    #highest value means highest precedence
    # ~: logical negation, &: and, |: or, >: implication, =: equivalence
    prec = {'~': 3, '&': 2, '|': 1, '>': 0, '=': 0}
    allowed = ['~','&','|','>','=','(',')']

    """rl_associative as in operation is read from right-to-left 
    ie. right-associative"""
    rl_associative = None
    """lr_asspciative as in operation is read from left-to-right
    ie. left-associative"""
    lr_associative = None

    assoc = {'~': rl_associative, '&': lr_associative,
            '|': lr_associative, '>': lr_associative, '=': lr_associative}

    opstack = []
    postfix = []

    # todo: error handling for concatenated variables

    if len(expression) == 0:
        raise SyntaxError("Empty input!")

    if not any(token.isalpha() for token in expression):
        raise SyntaxError("Expression does not contain any variables, please check your input!")

    for token in expression:
        if token.isalpha():
            postfix.append(token)

        if token not in allowed and not token.isalpha():
            raise SyntaxError(f"Expression contains invalid character: {token}, please check your input!")

        if token in prec:
            while len(opstack) > 0 and opstack[-1] != '(' and (prec[token] < prec[opstack[-1]] or
            (prec[token] == prec[opstack[-1]] and
            assoc[token] == lr_associative)):
                postfix.append(opstack.pop())
            opstack.append(token)

        elif token == '(':
            opstack.append(token)

        elif token == ')':
            #If opstack is empty, there are mismatched brackets
            if len(opstack) == 0 or opstack[-1] == ')':
                raise SyntaxError("Expression contains mismatched brackets, please check your input!")
            while opstack[-1] != '(' and len(opstack) > 0:
                postfix.append(opstack.pop())
            opstack.pop()

    while len(opstack) > 0 and opstack[-1] != '(':
        #If opstack[-1] == '(', there are mismatched brackets
        postfix.append(opstack.pop())
    if '(' in opstack:
        raise SyntaxError("Expression contains mismatched brackets, please check your input!")

    return postfix
