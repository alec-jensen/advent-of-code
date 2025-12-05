with open("2025/day5.txt") as f:
    data = f.read().strip()

ranges = data.split("\n\n")[0].splitlines()
ids = [int(x) for x in data.split("\n\n")[1].splitlines()]

total = 0

for i in ids:
    for r in ranges:
        lower, upper = [int(x) for x in r.split("-")]

        if not (lower <= i <= upper):
            continue

        total += 1
        break

print(total)