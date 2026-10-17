from heapq import heapify, heapreplace


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        smallest = float("inf")

        for value in nums:
            if value % 2 == 1:
                value *= 2

            heap.append(-value)
            smallest = min(smallest, value)

        heapify(heap)
        best = float("inf")

        while True:
            largest = -heap[0]
            best = min(best, largest - smallest)

            if best == 0 or largest % 2 == 1:
                break

            reduced = largest // 2
            smallest = min(smallest, reduced)
            heapreplace(heap, -reduced)

        return best