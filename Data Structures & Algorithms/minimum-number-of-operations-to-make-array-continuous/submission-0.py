class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        unique = sorted(set(nums))
        left = 0
        most_kept = 0

        for right, value in enumerate(unique):
            while value - unique[left] >= n:
                left += 1

            most_kept = max(most_kept, right - left + 1)

        return n - most_kept