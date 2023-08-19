# Logic Calculator
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

This program is a calculator that utilizes the Shunting Yard algorithm. It can be used to create a truth table for a propositional logic formula or convert the formula to either [Disjunctive Normal Form (DNF-form)](https://en.wikipedia.org/wiki/Disjunctive_normal_form) or [Conjunctive Normal Form (CNF form)](https://en.wikipedia.org/wiki/Conjunctive_normal_form). A propositional formula in DNF consists of disjunctions of conjunctions, while CNF consists of conjunctions of disjunctions. Especially CNF is useful in automated proof systems, such as [resolution](https://en.wikipedia.org/wiki/Resolution_(logic)). CNF and DNF forms for any formula can be directly derived from the truth table of the formula.

## How to Use
1. Download dependencies: `poetry install`
2. Start application: `poetry run invoke start`
3. A guide will open up in the terminal, provide your input
4. Quit with input `quit`

### Example Inputs
- `table ~(a&b)|c` - Truth table of expression "not(a and b) or c"
- `cnf (a>b)=~(~a)` - CNF form of expression "(a implies b) equals not(not a)"
- `dnf (h|f)>i` - DNF form of expression "(h or f) implies i"
- `postfix k&m` - Postfix notation of expression "k and m"

## General Information
### Input
- Input operation in lowercase 
- Variables can be letters a-z in upper- or lowercase
- Double negation is supported when bracketed i.e `~(~a)` is ok, `~~a` is not okay
- Do not use spaces i.e `a&b` is okay, `a & b` is not okay
- Concatenated variables are not allowed i.e `ab` is an invalid variable
- Expressions are read from left to right if not bracketed, for example "h|f>i" is interpreted as "(h|f)>i"
- Expression can contain excess brackets as long as they match, for example `((a))` is valid, `(a))` is not valid

### CNF- and DNF-forms
CNF-form is derived from the truth table by choosing the rows where the expression is false, negating the values of the variables on that row and connecting them as in the example given:

Input: `table (a|c)>~(c&b)`

Output: 

    a | b | c | (a|c)>~(c&b) 
    ========================
    0 | 0 | 0 | 1           
    0 | 0 | 1 | 1           
    0 | 1 | 0 | 1           
    0 | 1 | 1 | 0           
    1 | 0 | 0 | 1           
    1 | 0 | 1 | 1           
    1 | 1 | 0 | 1           
    1 | 1 | 1 | 0           

Input: `cnf (a|c)>~(c&b)`

Output: 

    (a|~b|~c)&(~a|~b|~c)

<br>

DNF-form is derived from the truth table by choosing the rows where the expression is true and connecting them as in the example given:

Input: `dnf (a|c)>~(c&b)`

Output: 

    (~a&~b&~c)|(~a&~b&c)|(~a&b&~c)|(a&~b&~c)|(a&~b&c)|(a&b&~c)

## Documentation
- [Weekly report 1](Documentation/Viikkoraportit/Viikkoraportti1.md)
- [Weekly report 2](Documentation/Viikkoraportit/Viikkoraportti2.md)
- [Weekly report 3](Documentation/Viikkoraportit/Viikkoraportti3.md)
- [Weekly report 4](Documentation/Viikkoraportit/Viikkoraportti4.md)
- [Weekly report 5](Documentation/Viikkoraportit/Viikkoraportti5.md)
- [Specification document](Documentation/Specdocument.md)
- [Testing document](Documentation/Testingdocument.md)
- [Execution document](Documentation/Execdocument.md)
