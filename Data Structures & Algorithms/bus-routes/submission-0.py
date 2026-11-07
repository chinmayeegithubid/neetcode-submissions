from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)

        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus)

        if source not in stop_to_buses or target not in stop_to_buses:
            return -1

        queue = deque([source])
        visited_stops = {source}
        visited_buses = set()
        buses_taken = 0

        while queue:
            buses_taken += 1

            for _ in range(len(queue)):
                stop = queue.popleft()

                for bus in stop_to_buses[stop]:
                    if bus in visited_buses:
                        continue

                    visited_buses.add(bus)

                    for next_stop in routes[bus]:
                        if next_stop == target:
                            return buses_taken

                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append(next_stop)

        return -1