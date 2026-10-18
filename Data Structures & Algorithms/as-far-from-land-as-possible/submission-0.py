from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque(
            (r, c)
            for r in range(n)
            for c in range(n)
            if grid[r][c] == 1
        )

        if not queue or len(queue) == n * n:
            return -1

        distance = -1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    r, c = row + dr, col + dc

                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                        grid[r][c] = 1
                        queue.append((r, c))

            distance += 1

        return distance