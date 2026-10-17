from heapq import heappush, heappop


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        answer = [-1] * len(queries)
        waiting = [[] for _ in heights]

        for index, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a

            if a == b or heights[a] < heights[b]:
                answer[index] = b
            else:
                waiting[b].append((heights[a], index))

        heap = []

        for building, height in enumerate(heights):
            while heap and heap[0][0] < height:
                _, query_index = heappop(heap)
                answer[query_index] = building

            for query in waiting[building]:
                heappush(heap, query)

        return answer