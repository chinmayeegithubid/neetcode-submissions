from collections import deque
from typing import List

class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]],
        time: int, change: int
    ) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        shortest = [float("inf")] * (n + 1)
        second = [float("inf")] * (n + 1)

        shortest[1] = 0
        queue = deque([(1, 0)])

        while queue:
            node, steps = queue.popleft()

            if node == n and steps == second[n]:
                elapsed = 0

                for _ in range(steps):
                    # Odd intervals are red: wait for green.
                    if (elapsed // change) % 2 == 1:
                        elapsed = (elapsed // change + 1) * change

                    elapsed += time

                return elapsed

            next_steps = steps + 1

            for neighbor in graph[node]:
                if next_steps < shortest[neighbor]:
                    shortest[neighbor] = next_steps
                    queue.append((neighbor, next_steps))

                elif shortest[neighbor] < next_steps < second[neighbor]:
                    second[neighbor] = next_steps
                    queue.append((neighbor, next_steps))

        return -1