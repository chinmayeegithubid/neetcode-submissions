from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Direction values: 1=right, 2=left, 3=down, 4=up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = 0

        queue = deque([(0, 0, 0)])  # cost, row, column

        while queue:
            cost, r, c = queue.popleft()

            if cost != dist[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return cost

            for direction, (dr, dc) in enumerate(directions, 1):
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                extra = int(grid[r][c] != direction)
                new_cost = cost + extra

                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    state = (new_cost, nr, nc)

                    if extra == 0:
                        queue.appendleft(state)
                    else:
                        queue.append(state)

        return -1