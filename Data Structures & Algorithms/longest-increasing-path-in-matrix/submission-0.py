from collections import deque
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        indegree = [[0] * cols for _ in range(rows)]
        queue = deque()

        # Count smaller neighbors leading into each cell.
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and matrix[nr][nc] < matrix[r][c]
                    ):
                        indegree[r][c] += 1

                if indegree[r][c] == 0:
                    queue.append((r, c))

        length = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and matrix[nr][nc] > matrix[r][c]
                    ):
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            queue.append((nr, nc))

            length += 1

        return length