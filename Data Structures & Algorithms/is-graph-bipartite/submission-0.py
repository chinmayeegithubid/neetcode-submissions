class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)

        for start in range(len(graph)):
            if colors[start] != -1:
                continue

            colors[start] = 0
            stack = [start]

            while stack:
                node = stack.pop()

                for neighbor in graph[node]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[node]
                        stack.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False

        return True