class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = max(m, n), min(m, n)
        dp = [1] * cols

        for _ in range(1, rows):
            for col in range(1, cols):
                dp[col] += dp[col - 1]

        return dp[-1]