from collections import deque
from heapq import heappush, heappop

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        distance = [[-1] * n for _ in range(n)]
        queue = deque()

        # Find each cell's distance to its nearest thief.
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    distance[r][c] = 0
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr, nc))

        # Explore paths with the highest safeness first.
        best = [[-1] * n for _ in range(n)]
        best[0][0] = distance[0][0]
        heap = [(-distance[0][0], 0, 0)]

        while heap:
            negative_safeness, r, c = heappop(heap)
            safeness = -negative_safeness

            if safeness < best[r][c]:
                continue

            if r == n - 1 and c == n - 1:
                return safeness

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    candidate = min(safeness, distance[nr][nc])

                    if candidate > best[nr][nc]:
                        best[nr][nc] = candidate
                        heappush(heap, (-candidate, nr, nc))

        return 0