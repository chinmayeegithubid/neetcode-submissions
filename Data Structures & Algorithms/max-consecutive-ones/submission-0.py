class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = longest = 0

        for num in nums:
            if num == 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 0

        return longest