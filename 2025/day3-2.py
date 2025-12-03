with open("2025/day3.txt") as f:
    data = f.read().splitlines()

total = 0

for line in data:
    joltages = list(line)

    joltage = ""
    remaining = joltages.copy()

    for i in range(1, 13):
        if len(joltage) + len(remaining) == 12:
            joltage += "".join(remaining)
            break

        largest: str = ""

        for j in range(len(remaining)):
            candidate = remaining[j]
            digits_left = len(remaining) - j - 1
            if digits_left + len(joltage) >= 11:
                if candidate > largest:
                    largest = candidate

        joltage += largest
        largest_index = remaining.index(largest)
        remaining = remaining[largest_index + 1 :]

    total += int(joltage)

print(total)