from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_cost = [float("inf")] * n
        min_cost[0] = 0
        total = 0

        for _ in range(n):
            # Find the cheapest point to add to the tree.
            current = -1
            for i in range(n):
                if not visited[i]:
                    if current == -1 or min_cost[i] < min_cost[current]:
                        current = i

            visited[current] = True
            total += min_cost[current]

            # Update connection costs for remaining points.
            x, y = points[current]
            for j in range(n):
                if not visited[j]:
                    distance = (
                        abs(x - points[j][0]) +
                        abs(y - points[j][1])
                    )
                    min_cost[j] = min(min_cost[j], distance)

        return total