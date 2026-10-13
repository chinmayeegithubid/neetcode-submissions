from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        return all(count % 2 == 0 for count in counts.values())