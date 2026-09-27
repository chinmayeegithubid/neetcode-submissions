import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting = Counter(nums)
        heap = [ (-count,num)
            for num,count in counting.items()

        ]
        heapq.heapify(heap)
        return [ heapq. heappop(heap)[1] for i in range(k) ]
        