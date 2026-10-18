from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        start = next(
            (r, c)
            for r in range(n)
            for c in range(n)
            if grid[r][c] == 1
        )

        stack = [start]
        grid[start[0]][start[1]] = 2
        queue = deque()

        while stack:
            r, c = stack.pop()
            queue.append((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    stack.append((nr, nc))

        flips = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue

                    if grid[nr][nc] == 1:
                        return flips

                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))

            flips += 1

        return -1