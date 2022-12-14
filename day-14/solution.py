lines = [s.strip() for s in open("./input.txt").readlines()]

# '#' -> rock
# 'o' -> sand
# '.' -> air

def get_direction(src, dest):
    if dest > src:
        return 1
    else:
        return -1

def draw_line(graph, srcX, srcY, destX, destY):
    if srcX == destX:
        # Same X, draw vertical line?
        direction = get_direction(srcY, destY)
        current = srcY
        while current != destY:
            graph[(srcX, current)] = '#'
            current += direction

        graph[(srcX, current)] = '#'
    elif srcY == destY:
        # Same y, draw horizontal.
        direction = get_direction(srcX, destX)
        current = srcX
        while current != destX:
            graph[(current, srcY)] = '#'
            current += direction
        graph[(current, srcY)] = '#'
    pass

def map_graph():
    graph = {}
    for line in lines:
        coords = line.split(" -> ")
        for i in range(0, len(coords) - 1):
            srcX, srcY = [int(s) for s in coords[i].split(",")]
            destX, destY = [int(s) for s in coords[i + 1].split(",")]
            draw_line(graph, srcX, srcY, destX, destY)
    return graph

def find_max_y(graph):
    max_y = 0
    for k in graph:
        max_y = max(max_y, k[1])
    return max_y

# Returns whether it overflew.
def drop_sand(graph, max_y, start = (500, 0), floor = False):
    while start not in graph: # Air not in graph. Current is still air.
        start = (start[0], start[1] + 1) # Go down one step.

        # If y ever goes over max_y, it has overflown.
        if start[1] >= max_y:
            if not floor:
                return True
            else:
                # There's a floor at max_y.
                graph[(start[0], start[1] - 1)] = 'o'
                return False

    # Now start is definitely on something that's not air. So backtrack once.
    start = (start[0], start[1] - 1)

    # If below is rock, stop.
    below = (start[0], start[1] + 1)
    block = graph.get(below, None)

    if block is not None:
        # It's a sand block, flow to left or right.
        left = (below[0] - 1, below[1])
        right = (below[0] + 1, below[1])

        if left not in graph:
            return drop_sand(graph, max_y, left, floor)

        if right not in graph:
            return drop_sand(graph, max_y, right, floor)

        graph[start] = 'o'
        return False
    else:
        raise KeyError()

def illustrate(graph, fromX, toX, max_y):
    print()
    for y in range(max_y + 1):
        for x in range(fromX, toX + 1):
            print(graph.get((x, y), '.'), end="")
        print()
    print()

def solve_part_one():
    graph = map_graph()
    max_y = find_max_y(graph)

    units = 0
    done = False

    while not done:
        units += 1
        done = drop_sand(graph, max_y)

    print(units - 1) # Don't count the long lost sand :(

def solve_part_two():
    graph = map_graph()
    max_y = find_max_y(graph) + 2

    units = 0
    while (500, 0) not in graph:
        units += 1
        drop_sand(graph, max_y, floor=True)

    print(units) # Count the one at (500, 0) also.

solve_part_one()
solve_part_two()
