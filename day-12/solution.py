lines = [s.strip() for s in open("./input.txt").readlines()]
width = len(lines[0])
height = len(lines)

start = (-1, -1)
end = (-1, -1)
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def find_ends():
    global start
    global end

    for y, line in enumerate(lines):
        s = line.find('S')
        e = line.find('E')
        if s >= 0:
            start = (s, y)
        if e >= 0:
            end = (e, y)

def get_elevation(spot):
    x, y = spot
    if lines[y][x] == 'S':
        return ord('a')
    elif lines[y][x] == 'E':
        return ord('z')
    else:
        return ord(lines[y][x])

def can_jump(start, end):
    end_x, end_y = end
    return end_x >= 0 and end_x < width and end_y >= 0 and end_y < height and get_elevation(end) - get_elevation(start) <= 1

def find_lowest(iterable, f_score):
    node = None
    min_so_far = float('inf')
    for item in iterable:
        if node is None or f_score.get(item, float('inf')) < min_so_far:
            node = item
            min_so_far = f_score.get(item, float('inf'))
    return node

def manhattan_distance(a, b):
    a_x, a_y = a
    b_x, b_y = b
    return abs(b_x - a_x) + abs(b_y - a_y)

def build_path(current, parents):
    path = []
    while current in parents:
        path.insert(0, current)
        current = parents[current]
    return path

def pathfind(start, end, condition=None):
    open_set = set([start])
    parents = {start: None}
    g_score = {}
    f_score = {}

    g_score[start] = 0
    f_score[start] = manhattan_distance(start, end)

    while len(open_set) > 0:
        current = open_set.pop()
        if current == end:
            return build_path(current, parents)

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if condition is not None and not condition(current, neighbor):
                continue

            tentative = g_score[current] + 1
            if tentative < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative
                parents[neighbor] = current
                open_set.add(neighbor)

    return []

def solve_part_one(find=True):
    if find:
        find_ends()
    print(len(pathfind(start, end, can_jump)) - 1)

def solve_part_two(find=True):
    if find:
        find_ends()

    min_so_far = float('inf')
    for y, line in enumerate(lines):
        for x in range(len(line)):
            if get_elevation((x, y)) != ord('a'):
                continue
            
            path = pathfind((x, y), end, can_jump)
            if len(path) == 0:
                continue

            min_so_far = min(len(path), min_so_far)
    print(min_so_far - 1)

solve_part_one()
solve_part_two(find=False)
