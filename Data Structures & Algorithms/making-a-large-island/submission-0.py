from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        areas = {}
        island_id = 2
        best = 0

        # Label islands using iterative DFS.
        for r in range(n):
            for c in range(n):
                if grid[r][c] != 1:
                    continue

                stack = [(r, c)]
                grid[r][c] = island_id
                area = 0

                while stack:
                    row, col = stack.pop()
                    area += 1

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if (
                            0 <= nr < n
                            and 0 <= nc < n
                            and grid[nr][nc] == 1
                        ):
                            grid[nr][nc] = island_id
                            stack.append((nr, nc))

                areas[island_id] = area
                best = max(best, area)
                island_id += 1

        # Try turning each water cell into land.
        for r in range(n):
            for c in range(n):
                if grid[r][c] != 0:
                    continue

                neighbors = set()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] > 1:
                            neighbors.add(grid[nr][nc])

                merged_area = 1 + sum(areas[i] for i in neighbors)
                best = max(best, merged_area)

        return best