with open("2025/day6.txt") as f:
    file = f.read().strip().splitlines()

    ops = file[-1].split()[::-1]

    data = [[] for _ in range(len(ops))]

    curr_col_idx = 0
    curr_col_vals = []
    for j in range(len(file[0])-1, -1, -1):
        all_spaces = True
        n = ""
        for i in range(len(file[:-1])):
            if file[i][j] != " ":
                all_spaces = False
            n += file[i][j]

        curr_col_vals.append(n)

        if all_spaces:
            curr_col_idx += 1
            continue

        data[curr_col_idx].append(n.strip())

total = 0

for i, p in enumerate(data):
    op = ops[i]
    operands = [int(x) for x in p]

    res = operands[0]

    for o in operands[1:]:
        if op == "+":
            res += o
        elif op == "-":
            res -= o
        elif op == "*":
            res *= o
        elif op == "/":
            res /= o

    total += res

print(total)
