from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        # Find a meeting point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find the cycle entry (the duplicate)
        finder = 0
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return finder