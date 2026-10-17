from heapq import heapify, heapreplace
from math import isqrt


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-pile for pile in gifts]
        heapify(heap)

        for _ in range(k):
            largest = -heap[0]

            if largest == 1:
                break

            heapreplace(heap, -isqrt(largest))

        return -sum(heap)