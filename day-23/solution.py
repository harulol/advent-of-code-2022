elves = set()
directions = { 'N': (0, -1), 'NE': (1, -1), 'E': (1, 0), 'SE': (1, 1), 'S': (0, 1), 'SW': (-1, 1), 'W': (-1, 0), 'NW': (-1, -1) }
order = ['N', 'S', 'W', 'E']

def read_input():
    elves.clear()
    lines = [s.strip() for s in open("./input.txt").readlines()]
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                elves.add((x, y))

def add(a, b):
    return tuple(sum(i) for i in zip(a, b))

def neighbors(current, value=""):
    return [add(current, v) for d, v in directions.items() if value in d]

def propose(current):
    if all([neighbor not in elves for neighbor in neighbors(current)]):
        return current
    for consider in order:
        if all([neighbor not in elves for neighbor in neighbors(current, consider)]):
            return add(current, directions[consider])
    
    return current

def spread():
    destinations = {}
    proposals = set()
    movement = False

    for elf in elves:
        proposal = propose(elf)
        if proposal == elf:
            continue
        if proposal in proposals:
            destinations = {k:v for k, v in destinations.items() if v != proposal}
            continue
        proposals.add(proposal)
        destinations[elf] = proposal

    first = order.pop(0)
    order.append(first)

    for elf, destination in destinations.items():
        movement = True
        elves.remove(elf)
        elves.add(destination)

    return movement

def find_endpoints():
    return tuple([min(elf[0] for elf in elves), min(elf[1] for elf in elves)]), tuple([max(elf[0] for elf in elves), max(elf[1] for elf in elves)])

def solve_part_one():
    read_input()
    for _ in range(10):
        spread()

    min_point, max_point = find_endpoints()
    space = 0

    for y in range(min_point[1], max_point[1] + 1):
        for x in range(min_point[0], max_point[0] + 1):
            if (x, y) not in elves:
                space += 1

    print(space)

def solve_part_two():
    read_input()
    step = 1
    while spread():
        print(f"Current {step=}")
        step += 1

    print(step)

solve_part_two()
