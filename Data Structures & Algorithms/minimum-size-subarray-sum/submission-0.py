class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        shortest = len(nums) + 1

        for right, num in enumerate(nums):
            total += num

            while total >= target:
                shortest = min(shortest, right - left + 1)
                total -= nums[left]
                left += 1

        return shortest if shortest <= len(nums) else 0