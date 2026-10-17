from heapq import heappush, heappop


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        heap = []
        total = 0
        best = 0

        for minimum, value in pairs:
            heappush(heap, value)
            total += value

            if len(heap) > k:
                total -= heappop(heap)

            if len(heap) == k:
                best = max(best, total * minimum)

        return best