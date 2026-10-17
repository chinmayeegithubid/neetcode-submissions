from heapq import heapify, heappush, heappop


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapify(available)

        busy = []
        result = []
        time = 0

        for arrival, duration in enumerate(tasks):
            time = max(time, arrival)

            if not available:
                time = max(time, busy[0][0])

            while busy and busy[0][0] <= time:
                _, weight, index = heappop(busy)
                heappush(available, (weight, index))

            weight, index = heappop(available)
            result.append(index)
            heappush(busy, (time + duration, weight, index))

        return result