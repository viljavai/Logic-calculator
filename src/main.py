import sys
import traceback
from shunting_yard import shunting_yard
from truth_table import create_truth_table, evaluate

def main():
    guide= '''
    =======================================
    |            Operators                 |
    =======================================
    |  variables    |  Upper- and lower-   |
    |               |  case letters a-z    |
    ---------------------------------------
    |       &       |       AND            |
    ---------------------------------------
    |       |       |        OR            |
    ---------------------------------------
    |       >       |    implication       |
    ---------------------------------------
    |       =       |    equivalence       |
    ---------------------------------------

    =======================================
    |             Operations               |
    =======================================
    ---------------------------------------
    |     table     |Gives truth table for |
    |               | the given expression |
    ---------------------------------------
    |     CNF       |   Gives expression   |
    |               |     in CNF-form      |
    ---------------------------------------
    |     DNF       |   Gives expression   |
    |               |     in DNF-form      |
    ---------------------------------------
    |    postfix    |Gives given expression|
    |               | in postfix notation  |
    =======================================

    o Give input in form <operation> <expression>
    o Quit with input "quit"
    o Double negation is supported when bracketed i.e ~(~a) is ok, ~~a is not okay
    o Do not use spaces i.e a&b is okay, a & b is not okay

    '''
    print(guide)
    while True:
        user_input = input("Enter an operation and expression: ")
        if user_input == "quit":
            break
        else:
            try:
                operation, expression = user_input.split(' ', 1)
                valid = ["table","postfix"]
                if operation not in valid:
                    raise ValueError("Invalid operation, check your input!")
            except:
                print("Invalid operation, check your input!")
                sys.exit(1)
            
        if operation == "table":
            try:
                postfix = shunting_yard(expression)
                create_truth_table(postfix, expression)
            except SyntaxError as error:
                print(str(error))
        
        elif operation == "postfix":
            try:
                print(shunting_yard(expression))
            except SyntaxError as error:
                print(str(error))

if __name__ == "__main__":
    main()
