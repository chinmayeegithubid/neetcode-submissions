from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for before, after in relations:
            before -= 1
            after -= 1
            graph[before].append(after)
            indegree[after] += 1

        finish = time.copy()
        queue = deque(i for i in range(n) if indegree[i] == 0)

        while queue:
            course = queue.popleft()

            for neighbor in graph[course]:
                finish[neighbor] = max(
                    finish[neighbor],
                    finish[course] + time[neighbor]
                )

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return max(finish)