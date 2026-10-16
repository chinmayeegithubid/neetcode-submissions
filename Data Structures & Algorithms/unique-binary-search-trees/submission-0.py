class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for nodes in range(1, n + 1):
            for left_size in range(nodes):
                right_size = nodes - 1 - left_size
                dp[nodes] += dp[left_size] * dp[right_size]

        return dp[n]