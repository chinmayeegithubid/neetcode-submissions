class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        for start in range(n):
            if visited[start]:
                continue

            stack = [start]
            visited[start] = True
            vertices = 0
            degree_sum = 0

            while stack:
                node = stack.pop()
                vertices += 1
                degree_sum += len(graph[node])

                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            if degree_sum == vertices * (vertices - 1):
                answer += 1

        return answer