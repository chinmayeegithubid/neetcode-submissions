from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        graph = {}

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    node = r * cols + c
                    graph[node] = []

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 1
                        ):
                            graph[node].append(nr * cols + nc)

        if not graph:
            return 0

        if len(graph) == 1:
            return 1

        root = next(iter(graph))
        discovery = {root: 0}
        low = {root: 0}
        parent = {root: None}
        children = {root: 0}
        has_cut = False

        # Iterative DFS avoids Python recursion-depth limits.
        stack = [(root, iter(graph[root]))]

        while stack:
            node, neighbors = stack[-1]
            neighbor = next(neighbors, None)

            if neighbor is not None:
                if neighbor not in discovery:
                    parent[neighbor] = node
                    children[node] += 1
                    children[neighbor] = 0

                    discovery[neighbor] = len(discovery)
                    low[neighbor] = discovery[neighbor]
                    stack.append((neighbor, iter(graph[neighbor])))

                elif neighbor != parent[node]:
                    low[node] = min(low[node], discovery[neighbor])

            else:
                stack.pop()
                p = parent[node]

                if p is not None:
                    low[p] = min(low[p], low[node])

                    if p != root and low[node] >= discovery[p]:
                        has_cut = True

        # Some land was unreachable: already multiple islands.
        if len(discovery) != len(graph):
            return 0

        if children[root] > 1 or has_cut:
            return 1

        return 2