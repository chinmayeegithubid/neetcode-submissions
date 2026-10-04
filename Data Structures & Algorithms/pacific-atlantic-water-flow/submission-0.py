from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def explore(starts):
            visited = set(starts)
            stack = list(visited)

            while stack:
                r, c = stack.pop()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        stack.append((nr, nc))

            return visited

        pacific = explore(
            [(0, c) for c in range(cols)]
            + [(r, 0) for r in range(rows)]
        )

        atlantic = explore(
            [(rows - 1, c) for c in range(cols)]
            + [(r, cols - 1) for r in range(rows)]
        )

        return [[r, c] for r, c in pacific & atlantic]