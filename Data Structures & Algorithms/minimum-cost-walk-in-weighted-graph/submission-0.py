from typing import List

class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        parent = list(range(n))
        size = [1] * n

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a, b):
            root_a, root_b = find(a), find(b)

            if root_a == root_b:
                return

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

        # Build connected components.
        for u, v, weight in edges:
            union(u, v)

        # -1 is the identity for bitwise AND: -1 & weight == weight.
        component_and = [-1] * n

        for u, v, weight in edges:
            component_and[find(u)] &= weight

        result = []

        for start, end in query:
            root_start = find(start)
            root_end = find(end)

            if root_start != root_end:
                result.append(-1)
            else:
                result.append(component_and[root_start])

        return result