import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)
        result = [-1] * len(queries)
        heap = []
        i = 0

        for query, index in sorted((q, j) for j, q in enumerate(queries)):
            # Add intervals that start at or before this query.
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(heap, (right - left + 1, right))
                i += 1

            # Remove expired intervals from the heap's top.
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                result[index] = heap[0][0]

        return result