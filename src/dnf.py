def create_dnf(truth_table, variables):
    """Function that creates the DNF-form from the truth table of the given expression

    Args: 
        truth_table: The generated truth table
        variables(set): A set of variables used in the expression

    Returns:
        The DNF-form of the original expression
    """
    rows = truth_table.split("\n")
    dnf = []

    for row in rows[2:]:
        elements = row.split(" | ")
        # Choose all true rows and add variables as they are
        if elements[-1] == "1":
            term = []
            for i, val in enumerate(elements[:-1]):
                if val == "0":
                    term.append(f"~{variables[i]}")
                else:
                    term.append(f'{variables[i]}')
            dnf.append('&'.join(term))
    return '(' + ')|('.join(dnf) + ')'
