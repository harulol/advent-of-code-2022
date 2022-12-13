lines = [s.strip() for s in open("./input.txt").readlines()]
pairs = []
i = 0

while i < len(lines):
    pairs.append((eval(lines[i]), eval(lines[i + 1])))
    i += 3

# 0 = same, -1 = first < second, 1 = first > second
def is_in_order_p1(first, second) -> int:
    len1 = len(first)
    len2 = len(second)
    p1 = 0
    p2 = 0

    while p1 < len1 and p2 < len2:
        item1 = first[p1]
        item2 = second[p2]

        if isinstance(item1, list) or isinstance(item2, list):
            l1 = item1 if isinstance(item1, list) else [item1]
            l2 = item2 if isinstance(item2, list) else [item2]
            value = is_in_order_p1(l1, l2)
            if value != 0:
                return value
        else:
            if item1 > item2:
                return 1
            elif item1 < item2:
                return -1

        p1 += 1
        p2 += 1

    if len1 < len2:
        return -1
    elif len1 > len2:
        return 1
    else:
        return 0


# PART 1
correct_indices = 0
for i, pair in enumerate(pairs):
    if is_in_order_p1(pair[0], pair[1]) == -1:
        correct_indices += i + 1

print(correct_indices)


# PART 2
new_lines = [eval(s) for s in lines if len(s) > 0]
new_lines.extend([[[2]], [[6]]])
swapped = True
while swapped:
    swapped = False
    for i in range(len(new_lines) - 1):
        value = is_in_order_p1(new_lines[i], new_lines[i + 1])
        if value == 1:
            temp = new_lines[i]
            new_lines[i] = new_lines[i + 1]
            new_lines[i + 1] = temp
            swapped = True

print((new_lines.index([[2]]) + 1) * (new_lines.index([[6]]) + 1))
