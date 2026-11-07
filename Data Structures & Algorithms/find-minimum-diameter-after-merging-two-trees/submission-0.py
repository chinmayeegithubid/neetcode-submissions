from collections import deque
from typing import List

class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:

        def diameter(edges):
            n = len(edges) + 1
            graph = [[] for _ in range(n)]

            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            def bfs(start):
                distance = [-1] * n
                distance[start] = 0
                queue = deque([start])
                farthest = start

                while queue:
                    node = queue.popleft()
                    farthest = node

                    for neighbor in graph[node]:
                        if distance[neighbor] == -1:
                            distance[neighbor] = distance[node] + 1
                            queue.append(neighbor)

                return farthest, distance[farthest]

            endpoint, _ = bfs(0)
            _, length = bfs(endpoint)
            return length

        d1 = diameter(edges1)
        d2 = diameter(edges2)

        return max(d1, d2, (d1 + 1) // 2 + 1 + (d2 + 1) // 2)