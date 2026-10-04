from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        previous, current = 0, 0

        for money in nums:
            previous, current = current, max(current, previous + money)

        return current