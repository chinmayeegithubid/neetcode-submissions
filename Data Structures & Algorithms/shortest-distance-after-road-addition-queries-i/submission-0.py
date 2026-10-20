from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append(i + 1)

        answer = []

        for u, v in queries:
            graph[u].append(v)

            distance = [-1] * n
            distance[0] = 0
            queue = deque([0])

            while queue:
                city = queue.popleft()

                if city == n - 1:
                    break

                for neighbor in graph[city]:
                    if distance[neighbor] == -1:
                        distance[neighbor] = distance[city] + 1
                        queue.append(neighbor)

            answer.append(distance[n - 1])

        return answer