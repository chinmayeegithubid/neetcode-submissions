class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            gold = grid[r][c]
            grid[r][c] = 0
            best_next = 0

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                    best_next = max(best_next, dfs(nr, nc))

            grid[r][c] = gold
            return gold + best_next

        answer = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    answer = max(answer, dfs(r, c))

        return answer