class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        dp = [float("inf")] * cols
        dp[0] = 0

        for row in grid:
            for col in range(cols):
                above = dp[col]
                left = dp[col - 1] if col > 0 else float("inf")
                dp[col] = row[col] + min(above, left)

        return dp[-1]