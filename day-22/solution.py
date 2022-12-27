lines = [s.strip("\n") for s in open("./input.txt").readlines()]

map: dict[tuple[int, int], str] = {}
instructions: list[str] = []
directions = {'U': (0, -1), 'D': (0, 1), 'R': (1, 0), 'L': (-1, 0)}
cardinal = ['R', 'D', 'L', 'U']
start: tuple[int, int] = (-1, -1)

def parse_input():
    global start

    for y in range(len(lines) - 2):
        line = lines[y]
        for x, ch in enumerate(line):
            if x == 0 and start[0] < 0 and ch == '.':
                start = (x, y)
            if ch == '.' or ch == '#':
                map[(x, y)] = ch

    current = ""
    for ch in lines[-1]:
        if ch.isdigit():
            current += ch
            continue
        else:
            if len(current) > 0:
                instructions.append(current)
                current = ""
            instructions.append(ch)

    if len(current) > 0:
        instructions.append(current)

def find_destination(current: tuple[int, int], facing: str, to_go: int) -> tuple[int, int]:
    steps = 0
    print(f"Checking moving {to_go} steps, facing {facing} for {current=}")

    while steps < to_go:
        dir = directions[facing]
        next = (current[0] + dir[0], current[1] + dir[1])

        if next not in map:
            # Reverse directions and step.
            dir = (-dir[0], -dir[1])
            maybe = current

            while True:
                maybe = (maybe[0] + dir[0], maybe[1] + dir[1])
                if maybe not in map:
                    next = (maybe[0] - dir[0], maybe[1] - dir[1]) # Backtrack once now that we're out on the other side.
                    break

        if map[next] == '#':
            return current
        else:
            current = next
            steps += 1

    return current

def traverse():
    current = start
    facing = 'R'

    for instruction in instructions:
        if instruction == 'L':
            facing = cardinal[(cardinal.index(facing) - 1) % 4]
            print("Turning left")
            continue
        elif instruction == 'R':
            facing = cardinal[(cardinal.index(facing) + 1) % 4]
            print("Turning right")
            continue

        destination = find_destination(current, facing, int(instruction))
        current = destination

    print(f"Final Location: {current=}, Col: {current[0] + 1}, Row: {current[1] + 1}")
    print(f"Password: {1000 * (current[1] + 1) + 4 * (current[0] + 1) + cardinal.index(facing)}")

parse_input()
traverse()
