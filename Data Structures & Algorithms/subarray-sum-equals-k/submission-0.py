class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        frequencies = {0: 1}
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            result += frequencies.get(prefix_sum - k, 0)
            frequencies[prefix_sum] = frequencies.get(prefix_sum, 0) + 1

        return result