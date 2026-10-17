from heapq import heappush, heapreplace


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []

        for num in nums:
            entry = (len(num), num)

            if len(heap) < k:
                heappush(heap, entry)
            elif entry > heap[0]:
                heapreplace(heap, entry)

        return heap[0][1]