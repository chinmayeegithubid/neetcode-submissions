class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = [0] * 101
        pairs = 0

        for num in nums:
            pairs += counts[num]
            counts[num] += 1

        return pairs