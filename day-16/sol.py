import re

class Valve:
    id: str
    flow: int
    tunnels: list[str]

    def __init__(self, id: str, flow: int, tunnels: list[str]) -> None:
        self.id = id
        self.flow = flow
        self.tunnels = tunnels

    def __str__(self) -> str:
        return f"Valve(id={self.id},flow={self.flow},tunnels={self.tunnels})"

lines = [s.strip() for s in open("./input.txt").readlines()]
valves: dict[str, Valve] = {}
paths: dict[tuple[str, str], list[str]] = {}

def parse_input():
    regex = r'Valve (.+) has flow rate=(.+); tunnels? leads? to valves? (.+)'
    for line in lines:
        search = re.search(regex, line)
        if not search:
            raise TypeError()

        valve = Valve(search.group(1), int(search.group(2)), search.group(3).split(", "))
        valves[valve.id] = valve

def pathfind(start: str, end: str) -> list[str]:
    if (start, end) in paths:
        return paths[(start, end)]

    open_set = set([start])
    g_score = {start: 0}
    parents = {}

    while len(open_set) > 0:
        current = open_set.pop()

        if current == end:
            path = []
            while current in parents:
                path.insert(0, current)
                current = parents[current]
            
            paths[(start, end)] = path
            return path

        valve = valves[current]
        for tunnel in valve.tunnels:
            tentative = g_score[current] + 1
            if tentative < g_score.get(tunnel, float('inf')):
                g_score[tunnel] = tentative
                open_set.add(tunnel)
                parents[tunnel] = current

    return []

def find_best_valve(open_valves: dict[str, int], current_minute: int, limit: int, start: str) -> tuple[str, dict[str, int]]:
    score: dict[str, int] = {}
    for id, valve in valves.items():
        # Already opened or useless valve.
        if id in open_valves or valve.flow <= 0:
            print(f"Valve {id} is open or useless, moving on.")
            continue

        path = pathfind(start, id)
        steps = len(path)

        print(f"Path found from {start} to {id} => {path}")

        # Not enough time.
        if current_minute + steps > limit:
            print(f"Currently at {current_minute}, but need {steps} to reach. Useless.")
            continue

        score[id] = max(limit - current_minute - steps - 1, 0) * valve.flow
        print(f"Currently at {current_minute}m, if open {id} at {current_minute + steps + 1}m, we get {score[id]} pressure.")
    
    return (max(score.keys(), key=lambda s: score[s], default=""), score)

def solve_part_one():
    limit = 30
    minute = 0
    current = "AA"
    opened_valves: dict[str, int] = {}

    while minute <= limit:
        best_valve, map = find_best_valve(opened_valves, minute, limit, current)
        if best_valve == "":
            break

        if minute == 0:
            best_valve = "DD"
            
        path = len(pathfind(current, best_valve))
        minute += path + 1
        opened_valves[best_valve] = minute
        current = best_valve

    total = 0
    for id, minute in opened_valves.items():
        valve = valves[id]
        total += (limit - minute) * valve.flow
    return total

parse_input()
print(solve_part_one())
