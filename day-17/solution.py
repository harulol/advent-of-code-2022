rocks = [
    ["####"], # - rock
    [" # ", "###", " # "], # + rock
    ["  #", "  #", "###"], # L rock?
    ["#", "#", "#", "#"], # | rock
    ["##", "##"], # cube rock
]
jets = open("./input.txt").readline()
directions = {'v': (0, -1), '<': (-1, 0), '>': (1, 0)}

def add(a, b):
    return tuple([a_i + b_i for a_i, b_i in zip(a, b)])

def get_highest(mappings):
    if len(mappings) == 0:
        return 0
    return max([coord[1] for coord in mappings.keys() if mappings[coord] == '#']) + 1

def illustrate(mappings):
    highest = get_highest(mappings)
    for y in range(highest + 3, -1, -1):
        print("|", end="")
        for x in range(0, 7):
            print("#" if (x, y) in mappings else ".", end="")
        print("|")
    print("+-------+")

def parse_rock(rock, mappings):
    highest = get_highest(mappings)
    current = set()

    for y, line in enumerate(reversed(rock)):
        for x, char in enumerate(line):
            if char == ' ':
                continue
            current.add((x + 2, highest + 3 + y))

    return current

def move(current, direction):
    return set([add(rock, directions[direction]) for rock in current])

def can_move(current, direction, mappings):
    destination = move(current, direction)
    return all([dest not in mappings and dest[0] >= 0 and dest[0] < 7 and dest[1] >= 0 for dest in destination])

def put_and_illustrate(current, mappings):
    for rock in current:
        mappings[rock] = '#'
    illustrate(mappings)
    for rock in current:
        del mappings[rock]

def drop_rock(rock, p_jet, mappings, debug=False):
    current = parse_rock(rock, mappings)

    if debug:
        print("Rock starts dropping")
        put_and_illustrate(current, mappings)
        print()

    while True:
        # Jet
        if can_move(current, jets[p_jet], mappings):
            current = move(current, jets[p_jet])

        if debug:
            print("Jet pushes rock to", jets[p_jet])
            put_and_illustrate(current, mappings)
            print()

        p_jet += 1
        p_jet %= len(jets)

        if not can_move(current, 'v', mappings):
            if debug:
                print("Rock comes to rest.")
                put_and_illustrate(current, mappings)
                print()
            break

        current = move(current, 'v')
        if debug:
            print("Rock drops down once")
            put_and_illustrate(current, mappings)
            print()

    for thing in current:
        mappings[thing] = '#'
    return p_jet

def solve_part_one():
    mappings = {}
    p_jet = 0    
    for i in range(2022):
        p_jet = drop_rock(rocks[i % 5], p_jet, mappings)
    print(get_highest(mappings))

solve_part_one()
