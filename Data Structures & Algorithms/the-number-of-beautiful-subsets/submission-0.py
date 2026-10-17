class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        chosen = {}

        def backtrack(index):
            if index == len(nums):
                return 1

            total = backtrack(index + 1)
            value = nums[index]

            if chosen.get(value - k, 0) == 0:
                chosen[value] = chosen.get(value, 0) + 1
                total += backtrack(index + 1)
                chosen[value] -= 1

            return total

        return backtrack(0) - 1