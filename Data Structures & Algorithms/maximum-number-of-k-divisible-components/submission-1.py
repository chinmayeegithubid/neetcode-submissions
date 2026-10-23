class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        order = [0]

        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        subtree_sum = values.copy()
        components = 0

        for node in reversed(order):
            if subtree_sum[node] % k == 0:
                components += 1
            elif parent[node] != -1:
                subtree_sum[parent[node]] += subtree_sum[node]

        return components