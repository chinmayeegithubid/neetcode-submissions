class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    continue

                stack = [(r, c)]
                grid[r][c] = 1
                closed = True

                while stack:
                    row, col = stack.pop()

                    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                        closed = False

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = row + dr, col + dc

                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            stack.append((nr, nc))

                if closed:
                    result += 1

        return result