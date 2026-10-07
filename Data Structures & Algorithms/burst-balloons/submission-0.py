from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        size = len(balloons)
        dp = [[0] * size for _ in range(size)]

        for gap in range(2, size):
            for left in range(size - gap):
                right = left + gap
                boundary_product = balloons[left] * balloons[right]

                for last in range(left + 1, right):
                    coins = (
                        dp[left][last]
                        + dp[last][right]
                        + boundary_product * balloons[last]
                    )
                    if coins > dp[left][right]:
                        dp[left][right] = coins

        return dp[0][size - 1]