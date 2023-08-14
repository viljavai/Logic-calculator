# Execution document
## Program structure
The program consists of functions for:
- parsing the inputted expression into postfix ("shunting_yard")
- creating a truth table from the postfix notation ("evaluate" for the logical steps, "create_truth_table" for
constructing the table and cosmetics)
- creating the CNF- and DNF-forms from the truth table ("create_cnf", "create_dnf").

## Time complexity
- As discussed in the specification document, the overall time complexity is O(2^m), where m is the number of variables in the input. This has been empirically tested with performance testing (see testing document).
- Space complexity is as discussed in the specification document.

## Future improvements
- The program does not give CNF- and DNF-forms in the nicest, most concise form possible. These forms are however logically equivalent (this can be checked in WolframAlpha). Possible improvement would be tidying up the input (however, I don't know if this can be done in a reasonable way with the method of forming the expressions from the truth table).
- Spaces and more diverse variables to be allowed in the input.

### Sources
- [Wikipedia - Shunting Yard Algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm) (pseudocode)
- Johdatus logiikkaan 1 -course material
