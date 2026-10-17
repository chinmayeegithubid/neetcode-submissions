from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        candidates = deque()
        best = nums[0]

        for i, value in enumerate(nums):
            while candidates and candidates[0][0] < i - k:
                candidates.popleft()

            current = value + max(0, candidates[0][1] if candidates else 0)
            best = max(best, current)

            while candidates and candidates[-1][1] <= current:
                candidates.pop()

            candidates.append((i, current))

        return best