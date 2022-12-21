lines = [s.strip() for s in open("./input.txt").readlines()]

def solve():
    total_surface = 0
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    cubes = set()

    for line in lines:
        x, y, z = [int(s) for s in line.split(",")]
        to_add = 6
        for direction in directions:
            neighbor = (x + direction[0], y + direction[1], z + direction[2])
            if neighbor in cubes:
                to_add -= 2
        cubes.add((x, y, z))
        total_surface += to_add

    print(total_surface)

    for cube in cubes:
        x, y, z = cube
        for direction in directions:
            neighbor = (x + direction[0], y + direction[1], z + direction[2])
            if neighbor in cubes:
                break
        else:
            total_surface -= 4

    print(total_surface)

solve()
