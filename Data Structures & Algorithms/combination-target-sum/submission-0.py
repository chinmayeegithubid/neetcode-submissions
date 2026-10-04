from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        combination = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(combination.copy())
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                combination.append(nums[i])
                backtrack(i, remaining - nums[i])
                combination.pop()

        backtrack(0, target)
        return result