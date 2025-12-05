# this one is pretty ugly, sorry in advance if you are trying to read it

with open("2025/day5.txt") as f:
    data = f.read().strip()

ranges = data.split("\n\n")[0].splitlines()

combined_ranges = []
excluded_ranges = set()

prev_combined = []

def check_overlap(r, c):
    l_r, u_r = [int(x) for x in r.split("-")]
    l_c, u_c = [int(x) for x in c.split("-")]

    # if ranges overlap, combine them and add to combined_ranges
    # then make sure to not double count them later

    # CASE 1: r overlaps c on the left
    if (l_r <= l_c <= u_r) and (u_c >= u_r):
        return True

    # CASE 2: r overlaps c on the right
    elif (l_c <= l_r) and (l_r <= u_c <= u_r):
        return True

    # CASE 3: r completely covers c
    elif (l_r <= l_c) and (u_c <= u_r):
        return True

    # CASE 4: c completely covers r
    elif (l_c <= l_r) and (u_r <= u_c):
        return True
    
    # CASE 5&6: r and c do not overlap
    elif ((l_r < l_c) and (u_r < l_c)) or ((l_c < l_r) and (u_c < l_r)):
        return False

for r in ranges:
    if r in excluded_ranges:
        continue

    l_r, u_r = [int(x) for x in r.split("-")]

    overlappers = []

    for c in ranges:
        if c in excluded_ranges:
            continue
        if c == r:
            excluded_ranges.add(c)
            continue

        if check_overlap(r, c):
            overlappers.append(c)

    # Find any further overlappers of the overlappers
    for c in overlappers:
        for j in ranges:
            if j == r or j == c or j in excluded_ranges:
                continue

            if check_overlap(c, j) and j not in overlappers:
                overlappers.append(j)

    if overlappers:
        all_lowers = [l_r]
        all_uppers = [u_r]

        for o in overlappers:
            l_o, u_o = [int(x) for x in o.split("-")]
            all_lowers.append(l_o)
            all_uppers.append(u_o)
            excluded_ranges.add(o)

        new_lower = min(all_lowers)
        new_upper = max(all_uppers)

        new_range = f"{new_lower}-{new_upper}"

        combined_ranges.append(new_range)
        excluded_ranges.add(r)
    else:
        combined_ranges.append(r)

total = 0

for r in combined_ranges:
    lower, upper = [int(x) for x in r.split("-")]

    total += upper - lower + 1

print(total)