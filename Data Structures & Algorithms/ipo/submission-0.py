import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int,
                             profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        available = []
        i = 0
        n = len(projects)

        for _ in range(min(k, n)):
            while i < n and projects[i][0] <= w:
                heapq.heappush(available, -projects[i][1])
                i += 1

            if not available:
                break

            w -= heapq.heappop(available)

        return w