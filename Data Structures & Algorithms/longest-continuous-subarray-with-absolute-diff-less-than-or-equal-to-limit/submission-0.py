from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        left = 0
        longest = 0

        for right, value in enumerate(nums):
            while min_queue and nums[min_queue[-1]] > value:
                min_queue.pop()
            while max_queue and nums[max_queue[-1]] < value:
                max_queue.pop()

            min_queue.append(right)
            max_queue.append(right)

            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if min_queue[0] == left:
                    min_queue.popleft()
                if max_queue[0] == left:
                    max_queue.popleft()
                left += 1

            longest = max(longest, right - left + 1)

        return longest