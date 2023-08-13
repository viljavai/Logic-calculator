def create_cnf(truth_table, variables):
    print(truth_table)
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
