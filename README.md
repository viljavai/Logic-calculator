# Logic calculator
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

The program is a calculator that utilizes the Shunting Yard algorithm. It can be used to create a truth table for a propositional logic formula or convert the formula to either disjunctive Normal Form [(DNF-form)](https://en.wikipedia.org/wiki/Disjunctive_normal_form) or conjunctive normal form [(CNF form)](https://en.wikipedia.org/wiki/Conjunctive_normal_form).  A propositional formula in DNF consists of disjunctions of conjunctions, while CNF consists of conjunctions of disjunctions. Especially CNF is useful in automated proof systems, such as [resolution](https://en.wikipedia.org/wiki/Resolution_(logic)). CNF and DNF forms for any formula can be directly derived from the truth table of the formula.

## How to use
1. Download dependencies <br>
`poetry install`
2. Start application <br>
`poetry run invoke start`
3. Guide will open up in the terminal, give your input
4. Quit with input "quit"

### Example inputs
- table ~(a&b)|c 
    > truth table of expression "not(a and b) or c"
- cnf (a>b)=~(~a)
    > cnf form of expression "(a implies b) equals not(not a)"
- dnf (h|f)>i
    > dnf form of expression "(h or f) implies i"
- postfix k&m
    > postfix notation of expression "k and m"

## General information
### Input
- Input operation in lowercase 
- Variables can be letters a-z in upper- or lowecase
- Quit with input "quit"
- Double negation is supported when bracketed i.e ~(~a) is ok, ~~a is not okay
- Do not use spaces i.e a&b is okay, a & b is not okay
- Concatenated variables are not allowed i.e ab is an invalid variable
- Expressions are read from left to right if not bracketed, for example "h|f>i" is interpreted as "(h|f)>i"
- Expression can contain excess brackets as long as they match, for example ((a)) is valid, (a)) is not valid

### CNF- and DNF-forms
- CNF-form is derived from the truth table by choosing the rows where the expression is false, negating the values of the variables on that row and connecting them as in the example given:
    > input: <br>
    > table (a|c)>~(c&b)<br>
    > output: <br>
    a | b | c | (a|c)>~(c&b)<br>
    ==============<br>
    0 | 0 | 0 | 1<br>
    0 | 0 | 1 | 1<br>
    0 | 1 | 0 | 1<br>
    0 | 1 | 1 | 0<br>
    1 | 0 | 0 | 1<br>
    1 | 0 | 1 | 1<br>
    1 | 1 | 0 | 1<br>
    1 | 1 | 1 | 0

    > input: <br>
    > cnf (a|c)>~(c&b) <br>
    > output: <br>
    > (a|~b|~c)&(~a|~b|~c)

- DNF-form is derived from the truth table by choosing the rows where the expression is true and connecting them as in the example given:
    > input: <br>
    > dnf (a|c)>~(c&b) <br>
    > output: <br>
    > (~a&~b&~c)|(~a&~b&c)|(~a&b&~c)|(a&~b&~c)|(a&~b&c)|(a&b&~c)

## Documentation
- [Weekly report 1](Documentation/Viikkoraportit/Viikkoraportti1.md) <br>
- [Weekly report 2](Documentation/Viikkoraportit/Viikkoraportti2.md) <br>
- [Weekly report 3](Documentation/Viikkoraportit/Viikkoraportti3.md) <br>
- [Weekly report 4](Documentation/Viikkoraportit/Viikkoraportti4.md) <br>
- [Specification document](Documentation/Specdocument.md)
- [Testing document](Documentation/Testingdocument.md)
