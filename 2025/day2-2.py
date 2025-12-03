with open("2025/day2.txt") as f:
    data = f.read().replace("\n", "").split(",")

total = 0

for line in data:
    bounds = line.split("-")
    start = int(bounds[0])
    end = int(bounds[1])

    for i in range(start, end + 1):
        id = str(i)

        for k in range(1, len(id)):
            if len(id) % k == 0:
                if id[:k] * (len(id) // k) == id:
                    total += i
                    break

print(total)