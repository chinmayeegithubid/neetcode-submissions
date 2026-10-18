from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            row, col, length = queue.popleft()

            if row == n - 1 and col == n - 1:
                return length

            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue

                    r, c = row + dr, col + dc

                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                        grid[r][c] = 1
                        queue.append((r, c, length + 1))

        return -1