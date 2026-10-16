class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        parent = [-1] * n
        order = [0]

        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        needed = hasApple.copy()
        total = 0

        for node in reversed(order):
            if node != 0 and needed[node]:
                total += 2
                needed[parent[node]] = True

        return total