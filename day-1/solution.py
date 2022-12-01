lines = []
calories = []
count = 0

# Strip all lines of the '\n'
with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

for line in lines:
    if len(line) == 0:
        calories.append(count)
        count = 0
    else:
        count += int(line)

# For the last elf.
if count > 0:
    calories.append(count)

calories.sort()

# Solution to part 1, highest number.
print(calories[-1])

# Solution to part 2, sum of 3 highest numbers.
print(sum(calories[-3:]))
