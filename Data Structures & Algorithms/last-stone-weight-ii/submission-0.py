class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for weight in range(target, stone - 1, -1):
                dp[weight] = dp[weight] or dp[weight - stone]

        for weight in range(target, -1, -1):
            if dp[weight]:
                return total - 2 * weight