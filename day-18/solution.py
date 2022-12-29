cubes: set[tuple[int, int, int]] = set()
adjacents: dict[str, tuple[int, int, int]] = {
    'X+': (1, 0, 0),
    'X-': (-1, 0, 0),
    'Y+': (0, 1, 0),
    'Y-': (0, -1, 0),
    'Z+': (0, 0, 1),
    'Z-': (0, 0, -1),
}

def add_tuple(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(n) for n in zip(a, b))

def parse_input():
    lines = [s.strip() for s in open("./input.txt").readlines()]
    for line in lines:
        x, y, z = line.split(",")
        cubes.add((int(x), int(y), int(z)))

def solve_part_one():
    untouched = 0

    for cube in cubes:
        for direction in adjacents.values():
            neighbor = add_tuple(cube, direction)
            if neighbor not in cubes:
                untouched += 1

    print(untouched)

def is_legal_node(node: tuple[int, int, int], min_out: tuple[int, int, int], max_out: tuple[int, int, int]) -> bool:
    for i in range(3):
        if node[i] < min_out[i] or node[i] > max_out[i]:
            return False
    return True        

def get_surrounding_cube() -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    min_x = min_y = min_z = 100
    max_x = max_y = max_z = -100

    for cube in cubes:
        x, y, z = cube

        min_x = min(x, min_x)
        min_y = min(y, min_y)
        min_z = min(z, min_z)

        max_x = max(x, max_x)
        max_y = max(y, max_y)
        max_z = max(z, max_z)

    return (min_x - 1, min_y - 1, min_z - 1), (max_x + 1, max_y + 1, max_z + 1)

# Find all considered "outside air blocks".
def pathfind(min_point: tuple[int, int, int], max_point: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    open_set = set([])
    open_set.add(min_point)
    air = set()

    while len(open_set) > 0:
        current = open_set.pop()
        if not is_legal_node(current, min_point, max_point) or current in cubes or current in air:
            continue
        
        air.add(current)
        for direction in adjacents.values():
            neighbor = add_tuple(current, direction)
            open_set.add(neighbor)

    return air

def solve_part_two():
    area = 0
    min_point, max_point = get_surrounding_cube()
    air = pathfind(min_point, max_point)

    for cube in cubes:
        for dir in adjacents.values():
            neighbor = add_tuple(cube, dir)
            if neighbor in air:
                area += 1

    print(area)

parse_input()
solve_part_one()
solve_part_two()
