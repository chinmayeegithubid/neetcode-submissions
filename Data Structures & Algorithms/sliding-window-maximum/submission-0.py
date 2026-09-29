from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []

        for right, value in enumerate(nums):
            # Remove indices outside the current window.
            while queue and queue[0] <= right - k:
                queue.popleft()

            # Remove smaller or equal values from the back.
            while queue and nums[queue[-1]] <= value:
                queue.pop()

            queue.append(right)

            # Record the maximum once a full window exists.
            if right >= k - 1:
                result.append(nums[queue[0]])

        return result