class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        result = []

        for i, value in enumerate(nums):
            left_difference = value * i - left_sum
            right_sum = total - left_sum - value
            right_difference = right_sum - value * (n - i - 1)

            result.append(left_difference + right_difference)
            left_sum += value

        return result