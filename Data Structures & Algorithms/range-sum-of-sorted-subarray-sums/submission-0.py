from heapq import heapify, heappop, heappush


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        heap = [(nums[i], i) for i in range(n)]
        heapify(heap)
        result = 0

        for rank in range(1, right + 1):
            total, end = heappop(heap)

            if rank >= left:
                result = (result + total) % MOD

            if end + 1 < n:
                heappush(heap, (total + nums[end + 1], end + 1))

        return result