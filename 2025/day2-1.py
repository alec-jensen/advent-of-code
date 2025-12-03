with open("2025/day2.txt") as f:
    data = f.read().replace("\n", "").split(",")

total = 0

for line in data:
    bounds = line.split("-")
    start = int(bounds[0])
    end = int(bounds[1])

    for i in range(start, end + 1):
        id = str(i)

        # odd lengths cant contain two equal halves
        if len(id) % 2 != 0:
            continue

        beg = id[:len(id)//2]
        end = id[len(id)//2:]
        if beg == end:
            total += i

print(total)