from collections import defaultdict
from typing import List

class Solution:
    def numberOfGoodPaths(
        self, vals: List[int], edges: List[List[int]]
    ) -> int:
        n = len(vals)
        graph = [[] for _ in range(n)]
        groups = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node, value in enumerate(vals):
            groups[value].append(node)

        parent = list(range(n))
        size = [1] * n

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a, b):
            a, b = find(a), find(b)

            if a == b:
                return

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]

        result = n  # Every single node is a good path.

        for value in sorted(groups):
            # Complete all unions for this value before counting.
            for node in groups[value]:
                for neighbor in graph[node]:
                    if vals[neighbor] <= value:
                        union(node, neighbor)

            counts = defaultdict(int)

            for node in groups[value]:
                counts[find(node)] += 1

            for count in counts.values():
                result += count * (count - 1) // 2

        return result