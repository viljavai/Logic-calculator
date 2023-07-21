#Takes expression and parses into postfix

def ShuntingYard(expression):
    #highest value means highest precedence
    # ~: logical negation, &: and, |: or, >: implication, =: equivalence
    prec = {'~': 3, '&': 2, '|': 1, '>': 0, '=': 0}

    """RL_associative as in operation is read from right-to-left 
    ie. right-associative """
    RL_associative = None
    """LR_asspciative as in operation is read from left-to-right
    ie. left-associative """
    LR_associative = None

    assoc = {'~': RL_associative, '&': LR_associative, 
            '|': LR_associative, '>': LR_associative, '=': LR_associative}

    opstack = []
    postfix = []

    for token in expression:
        if token.isalpha() or token.isdigit():
            postfix.append(token)

        elif token in prec:
            while len(opstack) > 0 and opstack[-1] != '(' and (prec[token] < prec[opstack[-1]] or 
            (prec[token] == prec[opstack[-1]] and 
            assoc[token] == LR_associative)):
                postfix.append(opstack.pop())
            opstack.append(token)
            
        elif token == '(':
            opstack.append(token)

        elif token == ')':
            """If opstack is empty, there are mismatched brackets,
            error handling todo"""
            while len(opstack) > 0 and opstack[-1] != '(':
                postfix.append(opstack.pop())
            if len(opstack) > 0 and opstack[-1] == '(':
                opstack.pop()
                
    while len(opstack) > 0 and opstack[-1] != '(':
        """If opstack[-1] == '(', there are mismatched brackets,
            error handling todo"""
        postfix.append(opstack.pop())
    
    return postfix

print(ShuntingYard("~(A&B)|A"))
#output: ['A', 'B', '&', 'A', '|', '~'] This is correct!
print(ShuntingYard("((A|B)&(C|A))|(A|D)"))
#output ['A', 'B', '|', 'C', 'A', '|', '&', 'A', 'D', '|', '|'] Probably not correct?