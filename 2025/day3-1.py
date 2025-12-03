with open("2025/day3.txt") as f:
    data = f.read().splitlines()

total = 0

for line in data:
    joltages = [int(x) for x in list(line)]

    highest = 0

    for j, i in enumerate(joltages):
        for k in joltages[j + 1 :]:
            if int(str(i) + str(k)) > highest:
                highest = int(str(i) + str(k))

    total += highest

print(total)
