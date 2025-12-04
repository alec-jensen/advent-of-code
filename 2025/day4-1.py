with open("2025/day4.txt") as f:
    data = [list(i) for i in f.read().strip().splitlines()]

total = 0

for i in range(len(data)):
    row = data[i]
    n = len(row)

    for j in range(n):
        cell = row[j]

        if cell == ".":
            continue

        count_adjacent = 0

        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue

                ni = i + x
                nj = j + y

                if 0 <= ni < len(data) and 0 <= nj < n:
                    neighbor = data[ni][nj]
                    if neighbor == "@":
                        count_adjacent += 1

        if count_adjacent < 4:
            total += 1

print(total)