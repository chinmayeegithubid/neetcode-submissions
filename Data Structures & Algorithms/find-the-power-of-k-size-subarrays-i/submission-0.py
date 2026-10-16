class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        streak = 0

        for i, value in enumerate(nums):
            if i > 0 and value == nums[i - 1] + 1:
                streak += 1
            else:
                streak = 1

            if i >= k - 1:
                result.append(value if streak >= k else -1)

        return result