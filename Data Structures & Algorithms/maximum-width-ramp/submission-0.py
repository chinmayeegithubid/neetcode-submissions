class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for i, value in enumerate(nums):
            if not stack or value < nums[stack[-1]]:
                stack.append(i)

        widest = 0

        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                widest = max(widest, j - i)

        return widest