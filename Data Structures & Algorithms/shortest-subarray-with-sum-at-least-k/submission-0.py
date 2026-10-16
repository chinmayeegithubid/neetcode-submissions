from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        candidates = deque([(0, 0)])
        prefix = 0
        shortest = len(nums) + 1

        for i, value in enumerate(nums, 1):
            prefix += value

            while candidates and prefix - candidates[0][1] >= k:
                start, _ = candidates.popleft()
                shortest = min(shortest, i - start)

            while candidates and candidates[-1][1] >= prefix:
                candidates.pop()

            candidates.append((i, prefix))

        return shortest if shortest <= len(nums) else -1