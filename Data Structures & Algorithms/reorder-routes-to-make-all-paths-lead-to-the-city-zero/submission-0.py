class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        reversals = 0
        stack = [(0, -1)]

        while stack:
            city, parent = stack.pop()

            for neighbor, needs_reversal in graph[city]:
                if neighbor == parent:
                    continue

                reversals += needs_reversal
                stack.append((neighbor, city))

        return reversals