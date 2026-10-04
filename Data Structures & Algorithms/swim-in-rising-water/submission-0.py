import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        best = [[float("inf")] * n for _ in range(n)]
        best[0][0] = grid[0][0]

        heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            time, row, col = heapq.heappop(heap)

            if time > best[row][col]:
                continue

            if row == n - 1 and col == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < n and 0 <= nc < n:
                    new_time = max(time, grid[nr][nc])

                    if new_time < best[nr][nc]:
                        best[nr][nc] = new_time
                        heapq.heappush(heap, (new_time, nr, nc))

        return -1