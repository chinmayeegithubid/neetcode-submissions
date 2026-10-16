class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        balance = 0
        longest = 0

        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1

            if balance in first_seen:
                longest = max(longest, i - first_seen[balance])
            else:
                first_seen[balance] = i

        return longest