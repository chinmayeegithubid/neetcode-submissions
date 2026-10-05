from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for subtotal in range(target, num - 1, -1):
                dp[subtotal] = dp[subtotal] or dp[subtotal - num]

            if dp[target]:
                return True

        return False