from heapq import heappop, heappush
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007

        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        dist = [float("inf")] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1
        heap = [(0, 0)]  # travel time, intersection

        while heap:
            time, u = heappop(heap)

            if time != dist[u]:
                continue

            for v, travel_time in graph[u]:
                arrival = time + travel_time

                if arrival < dist[v]:
                    # A shorter route replaces all previous routes.
                    dist[v] = arrival
                    ways[v] = ways[u]
                    heappush(heap, (arrival, v))

                elif arrival == dist[v]:
                    # Another route with the same shortest time.
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]