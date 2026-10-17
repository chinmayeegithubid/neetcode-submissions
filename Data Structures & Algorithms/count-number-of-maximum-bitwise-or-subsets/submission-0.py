class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        for value in nums:
            target |= value

        def backtrack(index, current):
            if current == target:
                return 1 << (len(nums) - index)

            if index == len(nums):
                return 0

            return (
                backtrack(index + 1, current)
                + backtrack(index + 1, current | nums[index])
            )

        return backtrack(0, 0)