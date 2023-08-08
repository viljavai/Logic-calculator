def create_cnf(truth_table, variables):
    cnf = []
    for row in truth_table:
        if row[-1] == 0:
            term = []
            for i, val in enumerate(row[:-1]):
                if val:
                    term.append(f'~{variables[i]}')
                else:
                    term.append(f'{variables[i]}')
            cnf.append('|'.join(term))
    print(cnf)

    return '&'.join(cnf)

def create_cnf(truth_table, variables):
    # last_bools has all final boolean values of the expression
    rows = truth_table.split("\n")
    last_bools = []

    for row in rows:
        elements = row.split(" | ")
        last_bool = elements[-1]
        last_bools.append(last_bool)
    
    