
import sys
import re
from pprint import pprint


class Valve:
    """Class to model the state of the valve."""
    def __init__(self, label, flow, tunnels):
        self.label = label
        self.flow = flow
        self.tunnels = tunnels
        self.opened = 0

    def open(self, time):
        self.opened = time

    def __str__(self):
        return f"Valve {self.label}: {self.flow}, {'open' if self.opened else 'closed'}"

    def __repr__(self):
        return str(self)


def parse_lines(lines):
    """Read the input and derive the data."""
    pattern = re.compile(r"Valve (\w\w) has flow rate=(\d+); "
                         + "tunnels? leads? to valves? ([A-Z, ]*)")

    valves = []
    for line in lines:
        valve, flow_str, tunnels_str = pattern.match(line).groups()
        flow = int(flow_str, 10)
        tunnels = tunnels_str.split(", ")
        valves.append(Valve(valve, flow, tunnels))

    valves.sort(key=lambda v: v.flow, reverse=True)
    return valves


def get_map(valves):
    tunnels = [(one.label, two) for one in valves for two in one.tunnels]
    return tunnels


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    valves = parse_lines(lines)
    tunnels = get_map(valves)
    pprint(valves)
    pprint(tunnels)

