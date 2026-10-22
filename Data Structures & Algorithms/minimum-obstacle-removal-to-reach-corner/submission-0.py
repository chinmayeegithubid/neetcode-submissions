from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        distance = [[rows * cols] * cols for _ in range(rows)]
        distance[0][0] = 0

        queue = deque([(0, 0, 0)])  # obstacles removed, row, column
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            removed, r, c = queue.popleft()

            if removed != distance[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return removed

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    cost = grid[nr][nc]
                    candidate = removed + cost

                    if candidate < distance[nr][nc]:
                        distance[nr][nc] = candidate
                        state = (candidate, nr, nc)

                        if cost == 0:
                            queue.appendleft(state)
                        else:
                            queue.append(state)

        return distance[-1][-1]