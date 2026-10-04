import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for source, target, time in times:
            graph[source].append((target, time))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue

            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        answer = max(dist[1:])
        return answer if answer != float("inf") else -1