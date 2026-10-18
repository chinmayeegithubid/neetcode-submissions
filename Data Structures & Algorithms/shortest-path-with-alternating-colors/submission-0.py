from collections import deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[] for _ in range(n)] for _ in range(2)]

        for a, b in redEdges:
            graph[0][a].append(b)
        for a, b in blueEdges:
            graph[1][a].append(b)

        distance = [[-1, -1] for _ in range(n)]
        distance[0] = [0, 0]
        queue = deque([(0, 0), (0, 1)])

        while queue:
            node, last_color = queue.popleft()
            next_color = 1 - last_color

            for neighbor in graph[next_color][node]:
                if distance[neighbor][next_color] == -1:
                    distance[neighbor][next_color] = (
                        distance[node][last_color] + 1
                    )
                    queue.append((neighbor, next_color))

        return [
            min((d for d in pair if d != -1), default=-1)
            for pair in distance
        ]