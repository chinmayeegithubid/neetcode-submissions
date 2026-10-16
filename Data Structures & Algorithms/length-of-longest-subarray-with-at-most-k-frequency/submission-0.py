class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = {}
        left = 0
        longest = 0

        for right, value in enumerate(nums):
            counts[value] = counts.get(value, 0) + 1

            while counts[value] > k:
                counts[nums[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest