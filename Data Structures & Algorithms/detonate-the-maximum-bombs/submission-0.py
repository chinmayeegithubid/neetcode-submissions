class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i, (x1, y1, radius) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i != j and (x1 - x2) ** 2 + (y1 - y2) ** 2 <= radius ** 2:
                    graph[i].append(j)

        best = 0

        for start in range(n):
            visited = {start}
            stack = [start]

            while stack:
                bomb = stack.pop()

                for neighbor in graph[bomb]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            best = max(best, len(visited))

            if best == n:
                return best

        return best