with open("2025/day6.txt") as f:
    data = [x.split() for x in f.read().strip().splitlines()]

inverted = list(map(list, zip(*data)))

total = 0

for p in inverted:
    op = p[-1]
    operands = [int(x) for x in p[:-1]]

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