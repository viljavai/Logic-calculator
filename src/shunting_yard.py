def shunting_yard(expression):
    """Algorithm for parsing a logical expression to postfix notation

    Args: 
        expression(string) is a logical expression in infix notation

    Raises:
        SyntaxError if expression contains:
            - nothing
            - no variables
            - concatenated variables or operators
            - invalid variables or operators
            - mismatched brackets
    
    Returns:
        postfix(list) contains the expression in postfix notation
    """
    #highest value means highest precedence
    #~: logical negation, &: and, |: or, >: implication, =: equivalence"""
    prec = {'~': 3, '&': 2, '|': 1, '>': 0, '=': 0}
    allowed = ['~','&','|','>','=','(',')']

    #rl_associative as in operation is read from right-to-left
    #ie. right-associative
    rl_associative = None
    #lr_associative as in operation is read from left-to-right
    #ie. left-associative
    lr_associative = None

    assoc = {'~': rl_associative,
             '&': lr_associative,
            '|': lr_associative, 
            '>': lr_associative, 
            '=': lr_associative}

    opstack = []
    postfix = []
    previous_token = None


    if len(expression) == 0:
        raise SyntaxError("Empty input!")

    if not any(token.isalpha() for token in expression):
        raise SyntaxError(
        "Expression does not contain any variables, "
        "please check your input!")

    for token in expression:
        if token.isalpha():
            if previous_token is not None and previous_token.isalpha():
                raise SyntaxError(
                    f"Expression contains concatenated variables: "
                    f"{previous_token}{token}, please check your input!")
            postfix.append(token)

        if token in prec:
            if previous_token == token:
                raise SyntaxError(
                    f"Expression contains concatenated operators: "
                    f"{previous_token}{token}, please check your input!")
            while len(opstack) > 0 and opstack[-1] != '(' and (prec[token] < prec[opstack[-1]] or
            (prec[token] == prec[opstack[-1]] and
            assoc[token] == lr_associative)):
                postfix.append(opstack.pop())
            opstack.append(token)

        if token not in allowed and not token.isalpha():
            raise SyntaxError(
                f"Expression contains invalid character: "
                f"{token}, please check your input!")

        elif token == '(':
            opstack.append(token)

        elif token == ')':
            #If opstack is empty, there are mismatched brackets
            if len(opstack) == 0 or opstack[-1] == ')':
                raise SyntaxError(
                    "Expression contains mismatched brackets, "
                    "please check your input!")
            while len(opstack) > 0 and opstack[-1] != '(':
                postfix.append(opstack.pop())
            if len(opstack) > 0:
                opstack.pop()
            else:
                raise SyntaxError(
                    "Expression contains mismatched brackets, please check your input!")

        previous_token = token

    if '(' in opstack:
        raise SyntaxError(
            "Expression contains mismatched brackets, "
            "please check your input!")

    while len(opstack) > 0 and opstack[-1] != '(':
        #If opstack[-1] == '(', there are mismatched brackets
        postfix.append(opstack.pop())


    return postfix
