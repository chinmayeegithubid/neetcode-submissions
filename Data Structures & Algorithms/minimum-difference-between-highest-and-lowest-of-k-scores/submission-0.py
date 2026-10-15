class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minimum = nums[k - 1] - nums[0]

        for i in range(1, len(nums) - k + 1):
            minimum = min(minimum, nums[i + k - 1] - nums[i])

        return minimum