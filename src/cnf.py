def create_cnf(truth_table, variables):
    """Function that creates the CNF-form from the truth table of the given expression

    Args: 
        truth_table: The generated truth table
        variables(set): A set of variables used in the expression

    Returns:
        The CNF-form of the original expression

    """
    rows = truth_table.split("\n")
    cnf = []

    for row in rows[2:]:
        elements = row.split(" | ")
        # Choose all false rows and add corresponding variables, negated
        if elements[-1] == "0":
            term = []
            for i, val in enumerate(elements[:-1]):
                if val == "1":
                    term.append(f"~{variables[i]}")
                else:
                    term.append(f'{variables[i]}')
            cnf.append('|'.join(term))
    return '(' + ')&('.join(cnf) + ')'
