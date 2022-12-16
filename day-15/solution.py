# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
import re

lines = [s.strip() for s in open("./input.txt").readlines()]
beacons = set()
sensors = {}
distances = {}

def manhattan_distance(a, b):
    aX, aY = a
    bX, bY = b
    return abs(bX - aX) + abs(bY - aY)

def parse_input():
    beacons.clear()
    sensors.clear()
    distances.clear()

    for line in lines:
        regexp = re.search(r'Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)', line)
        
        if not regexp:
            raise TypeError()

        beacon = (int(regexp.group(3)), int(regexp.group(4)))
        sensor = (int(regexp.group(1)), int(regexp.group(2)))
        beacons.add(beacon)
        sensors[sensor] = beacon
        distances[sensor] = manhattan_distance(sensor, beacon)

def can_reach(sensor, target):
    dist = distances[sensor]
    return manhattan_distance(sensor, target) <= dist

def impossible_beacon(y):
    visited = set()

    for sensor in sensors:
        current = (sensor[0], y)
        i = 0

        # Traverse left.
        while True:
            node = (current[0] + i, y)
            if can_reach(sensor, node):
                if node not in beacons and node not in sensors:
                    visited.add(node)
                i -= 1
            else: break

        # Traverse right
        i = 1
        while True:
            node = (current[0] + i, y)
            if can_reach(sensor, node):
                if node not in beacons and node not in sensors:
                    visited.add(node)
                i += 1
            else: break

    return len(visited)

def visualize(x_range, y_range):
    min_x, max_x = x_range
    min_y, max_y = y_range

    def check(x, y):
        node = (x, y)
        if node in beacons:
            print("B", end="")
        elif node in sensors:
            print("S", end="")
        else:
            char = '.'
            for sensor in sensors:
                if can_reach(sensor, node):
                    char = '#'
                    break
            print(char, end="")

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            check(x, y)
        print()

def scan(minimum, maximum):
    m = impossible_beacon(0)
    at = 0
    for y in range(minimum, maximum + 1):
        if y % 1000 == 0:
            print(f"Scanning line {y}")
        count = impossible_beacon(y)
        if m != count:
            at = y
            break

    return f"Y = {at}"

# Part 1
parse_input()
print(impossible_beacon(2000000))
