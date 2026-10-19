class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        stack = []

        def add_land(r, c):
            if grid[r][c] == 1:
                grid[r][c] = 0
                stack.append((r, c))

        for r in range(rows):
            add_land(r, 0)
            add_land(r, cols - 1)

        for c in range(cols):
            add_land(0, c)
            add_land(rows - 1, c)

        while stack:
            row, col = stack.pop()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r, c = row + dr, col + dc

                if 0 <= r < rows and 0 <= c < cols:
                    add_land(r, c)

        return sum(sum(row) for row in grid)