from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = current_min = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            current_max, current_min = (
                max(num, current_max * num, current_min * num),
                min(num, current_max * num, current_min * num)
            )

            result = max(result, current_max)

        return result