with open("2025/day1.txt") as f:
    data = f.read().strip().splitlines()

# 0-99 dial
dial = 50

password = 0

for line in data:
    direction = line[0]
    steps = int(line[1:])

    if direction == "L":
        dial -= steps
    elif direction == "R":
        dial += steps

    dial %= 100
    if dial == 0:
        password += 1

print(password)