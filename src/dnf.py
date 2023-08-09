def create_dnf(truth_table, variables):
    rows = truth_table.split("\n")
    dnf = []

    for row in rows[2:]:
        elements = row.split(" | ")
        if elements[-1] == "1":
            term = []
            for i, val in enumerate(elements[:-1]):
                if val == "0":
                    term.append(f"~{variables[i]}")
                else:
                    term.append(f'{variables[i]}')
            dnf.append('&'.join(term))
    return '(' + ')|('.join(dnf) + ')'
