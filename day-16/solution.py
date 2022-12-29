import re

lines = [s.strip() for s in open("./input.txt").readlines()]
valves = {}
paths_memo = {}

class Valve:
    name: str
    open_at: int
    flow_rate: int
    tunnels: set[str]

    def __init__(self, name, flow_rate) -> None:
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = set()
        self.open_at = 0

    def apply_tunnels(self, tunnels) -> None:
        self.tunnels.update(tunnels)

    def __str__(self) -> str:
        return f"Valve(name={self.name},open={self.open_at},flow={self.flow_rate},tunnels={self.tunnels})"

    def calculate_pressure(self, open_at, flow_rate, limit=30) -> int:
        if open_at <= 0:
            return 0
        return max(limit - open_at + 1, 0) * flow_rate

    @property
    def total_pressure(self) -> int:
        return self.calculate_pressure(self.open_at, self.flow_rate)

    # The value of finding another valve to open instead of opening this one right now.
    def opportunity_value(self, minutes):
        value = {}

        for name, valve in valves.items():
            if valve.open_at > 0 or valve.flow_rate == 0:
                value[name] = float('-inf')
                continue

            value[name] = self.calculate_pressure(minutes + pathfind(self.name, name) + 1, valve.flow_rate)
        return value

def parse_input():
    regex = r'Valve (.+) has flow rate=(.+); tunnels? leads? to valves? (.+)'
    for line in lines:
        match_obj = re.search(regex, line)
        if not match_obj:
            continue
        valve = Valve(match_obj.group(1), int(match_obj.group(2)))
        valve.apply_tunnels(match_obj.group(3).split(", "))
        valves[match_obj.group(1)] = valve

def max_value(value: dict[str, int]) -> str:
    valve = ""
    max_so_far = float('-inf')
    for k, v in value.items():
        if v > max_so_far:
            max_so_far = v
            valve = k
    return valve

def pathfind(start: str, target: str):
    if (start, target) in paths_memo:
        return paths_memo[(start, target)]

    open_set = set([start])
    parents = {}
    g_score = {}

    g_score[start] = 0

    while len(open_set) > 0:
        current = open_set.pop()
        if current == target:
            count = 1

            while current in parents:
                current = parents[current]
                count += 1

            paths_memo[(start, target)] = count - 1

            return count - 1
        
        valve = valves[current]
        for tunnel in valve.tunnels:
            tentative = g_score[current] + 1
            if tentative < g_score.get(tunnel, float('inf')):
                g_score[tunnel] = tentative
                parents[tunnel] = current
                open_set.add(tunnel)

    raise KeyError()

def solve_part_one():
    minutes_elapsed = 1
    current = "AA"

    while minutes_elapsed < 30:
        valve = valves[current]
        values = valve.opportunity_value(minutes_elapsed)
        best_valve = max_value(values)

        # No more need of movement, just terminate the loop.
        if best_valve == "":
            break

        print(f"Minutes = {minutes_elapsed}, Opportunity Cost = {values}")

        if best_valve == current:
            minutes_elapsed += 1

            if valve.open_at <= 0:
                valve.open_at = minutes_elapsed
                print(f"Opening valve {valve.name} at minutes {minutes_elapsed}")

            continue
        else:
            print(f"Currently {minutes_elapsed}m elapsed. Finding best way to go {current} => {best_valve}, in {pathfind(current, best_valve)} steps.")
            minutes_elapsed += pathfind(current, best_valve)
            current = best_valve

    print(sum([valve.total_pressure for _, valve in valves.items()]))

parse_input()
solve_part_one()
