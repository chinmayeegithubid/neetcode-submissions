class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        result = 0

        for right, value in enumerate(nums):
            window_sum += value

            while value * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1

            result = max(result, right - left + 1)

        return result