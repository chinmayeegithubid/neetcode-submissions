class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        current_max = maximum = nums[0]
        current_min = minimum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            current_max = max(num, current_max + num)
            maximum = max(maximum, current_max)

            current_min = min(num, current_min + num)
            minimum = min(minimum, current_min)

            total += num

        if maximum < 0:
            return maximum

        return max(maximum, total - minimum)