import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ordered = sorted(
            (enqueue, duration, index)
            for index, (enqueue, duration) in enumerate(tasks)
        )

        available = []
        result = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or available:
            if not available:
                time = max(time, ordered[i][0])

            while i < n and ordered[i][0] <= time:
                _, duration, index = ordered[i]
                heapq.heappush(available, (duration, index))
                i += 1

            duration, index = heapq.heappop(available)
            time += duration
            result.append(index)

        return result