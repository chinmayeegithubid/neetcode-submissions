class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        if max(nums) > target:
            return False

        n = len(nums)
        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue

            for i, num in enumerate(nums):
                if mask & (1 << i):
                    continue

                next_sum = dp[mask] + num
                if next_sum <= target:
                    next_mask = mask | (1 << i)
                    dp[next_mask] = next_sum % target

        return dp[-1] == 0