from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_range(start: int, end: int) -> int:
            previous, current = 0, 0

            for i in range(start, end):
                previous, current = current, max(
                    current, previous + nums[i]
                )

            return current

        return max(
            rob_range(0, len(nums) - 1),  # Exclude last house
            rob_range(1, len(nums))       # Exclude first house
        )