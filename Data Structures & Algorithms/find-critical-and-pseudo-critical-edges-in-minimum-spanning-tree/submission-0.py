class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        ordered = sorted(
            (weight, a, b, index)
            for index, (a, b, weight) in enumerate(edges)
        )

        def mst(skip: int = -1, force: int = -1) -> int:
            parent = list(range(n))
            size = [1] * n

            def find(node: int) -> int:
                while node != parent[node]:
                    parent[node] = parent[parent[node]]
                    node = parent[node]
                return node

            def union(a: int, b: int) -> bool:
                a, b = find(a), find(b)
                if a == b:
                    return False

                if size[a] < size[b]:
                    a, b = b, a

                parent[b] = a
                size[a] += size[b]
                return True

            total = 0
            used = 0

            if force != -1:
                a, b, weight = edges[force]
                union(a, b)
                total += weight
                used += 1

            for weight, a, b, index in ordered:
                if index == skip or index == force:
                    continue

                if union(a, b):
                    total += weight
                    used += 1

                if used == n - 1:
                    break

            return total if used == n - 1 else float("inf")

        baseline = mst()
        critical = []
        pseudo_critical = []

        for index in range(len(edges)):
            if mst(skip=index) > baseline:
                critical.append(index)
            elif mst(force=index) == baseline:
                pseudo_critical.append(index)

        return [critical, pseudo_critical]