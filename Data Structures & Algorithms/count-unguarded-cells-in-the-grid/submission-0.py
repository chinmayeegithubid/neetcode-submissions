class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0: empty, 1: wall, 2: guard, 3: watched
        grid = [[0] * n for _ in range(m)]

        for row, col in walls:
            grid[row][col] = 1

        for row, col in guards:
            grid[row][col] = 2

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for row, col in guards:
            for dr, dc in directions:
                r, c = row + dr, col + dc

                while 0 <= r < m and 0 <= c < n:
                    if grid[r][c] in (1, 2):
                        break

                    grid[r][c] = 3
                    r += dr
                    c += dc

        return sum(row.count(0) for row in grid)