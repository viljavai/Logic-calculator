## Specification Document

- The program will be implemented in Python. I am also able to peer review projects done in Java if needed, but not nearly as well as in Python.
- The program will utilize the Shunting Yard algorithm.
- The program will be able to generate truth tables, CNF (Conjunctive Normal Form), or DNF (Disjunctive Normal Form) representations for predicate logic formulas. The Shunting Yard algorithm is well-suited for this project as it handles arithmetic operations well and can be adapted for propositional logic.
- Inputs:
  > - "table A and B => A or C" This would output a tautology, which is a truth table with all TRUE values.
  > - "postfix A and B" This would output [A,B,and]
  > - "CNF (A and B) or C" This would output "(A or B) and (B or C)"
  > - "DNF (A or B) and C" This would output "(A and C) or (B and C)"
- Everything is in English, except weekly reports are in Finnish.
- The study program is TKT-kandi.

### Time Complexity Analysis

#### Time Complexity

- Processing the input using the Shunting Yard algorithm: O(n)
- If the input has m variables, the truth table will have 2^m rows. Thus, the time complexity of generating the truth table is O(2^m), where m is the number of variables in the input.

The overall time complexity is therefore **O(2^m)**.

#### Space Complexity
- Space complexity of the Shunting Yard algorithm: O(n)
- Space complexity of generating the truth table: O(2^m), where m is the number of variables in the input.

The overall space complexity is therefore **O(2^m)**.

### References:
- [Wikipedia - Shunting Yard Algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm) (pseudocode)
- (More references will be added)
