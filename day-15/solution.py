# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
import re
from typing import Union

lines: list[str] = [s.strip() for s in open("./input.txt").readlines()]

beacons: set[tuple[int, int]] = set() # Coords
sensors: dict[tuple[int, int], tuple[int, int]] = {} # Sensor -> Beacon
distances: dict[tuple[int, int], int] = {} # Sensor -> Distance

def manhattan_distance(source: tuple[int, int], destination: tuple[int, int]) -> int:
    a_x, a_y = source
    b_x, b_y = destination
    return abs(b_x - a_x) + abs(b_y - a_y)

def tuple_add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    a_x, a_y = a
    b_x, b_y = b
    return (a_x + b_x, a_y + b_y)

def parse_input():
    regex = r'Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)'
    for line in lines:
        search = re.search(regex, line)
        if not search:
            raise TypeError()

        beacon = (int(search.group(3)), int(search.group(4)))
        sensor = (int(search.group(1)), int(search.group(2)))

        beacons.add(beacon)
        sensors[sensor] = beacon
        distances[sensor] = manhattan_distance(beacon, sensor)

def overlaps(region: tuple[int, int], other: tuple[int, int]) -> Union[tuple[int, int], None]:
    start, end = region
    other_start, other_end = other

    if start >= other_start and start <= other_end:
        return (other_start, max(other_end, end))
    elif other_start >= start and other_start <= end:
        return (start, max(other_end, end))

    return None

def smoosh_all_regions(regions: list[tuple[int, int]]):
    i = 0
    while i < len(regions):
        for j in range(len(regions)):
            if i == j or i >= len(regions) or j >= len(regions):
                continue

            overlap = overlaps(regions[i], regions[j])

            if overlap:
                regions[i] = overlap
                regions.pop(j)

        i += 1

def is_in(number: int, region: tuple[int, int]) -> bool:
    start, end = region
    return number >= start and number <= end

def impossible_beacons(y: int) -> int:
    print("Starting the process to find impossible beacon places")
    regions = []

    for sensor in sensors:
        y_offset = abs(sensor[1] - y)
        if y_offset > distances[sensor]:
            continue
    
        min_x = sensor[0] - (distances[sensor] - y_offset)
        max_x = sensor[0] + (distances[sensor] - y_offset)
        current = (min_x, max_x)

        # Shallow matching.
        regions.append(current)
        smoosh_all_regions(regions)

    # Shallow count, also counting places where there already are beacons and sensors.
    count = 0
    for region in regions:
        count += region[1] - region[0] + 1
        for beacon, sensor in zip(beacons, sensors.keys()):
            if beacon[1] == y and is_in(beacon[0], region):
                count -= 1
            if sensor[1] == y and is_in(sensor[0], region):
                count -= 1

    return count

def find_distress_beacon(min_val: int, max_val: int) -> tuple[int, int]:   
    print("Starting to scan for the distress beacon")
    for y in range(min_val, max_val + 1):
        if y % 100000 == 0:
            print(f"Searching at {y=}")

        x = min_val
        while x <= max_val:
            for sensor in sensors:
                #print(f"Checking sensor {sensor} for {x=},{y=}")
                y_offset = abs(sensor[1] - y)
                if y_offset > distances[sensor]:
                    continue
    
                min_x = sensor[0] - (distances[sensor] - y_offset)
                max_x = sensor[0] + (distances[sensor] - y_offset)

                if x >= min_x and x <= max_x:
                    x = max_x + 1
                    break
            else:     
                return (x, y)
    
    return (min_val - 1, min_val - 1)

parse_input()

# PART ONE
print(impossible_beacons(2000000))

# PART TWO
distress_beacon = find_distress_beacon(0, 4000000)
print(distress_beacon[0] * 4000000 + distress_beacon[1])
