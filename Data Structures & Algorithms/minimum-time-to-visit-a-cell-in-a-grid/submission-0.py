from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # No legal first move.
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]  # time, row, column
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while heap:
            time, r, c = heappop(heap)

            if time != dist[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                arrival = time + 1
                unlock = grid[nr][nc]

                if arrival < unlock:
                    arrival = unlock + (unlock - arrival) % 2

                if arrival < dist[nr][nc]:
                    dist[nr][nc] = arrival
                    heappush(heap, (arrival, nr, nc))

        return -1