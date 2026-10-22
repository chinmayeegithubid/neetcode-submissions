from heapq import heapify, heappop, heappush

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])

        if rows < 3 or cols < 3:
            return 0

        visited = [[False] * cols for _ in range(rows)]
        heap = []

        # Water can escape through any boundary cell.
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    heap.append((heightMap[r][c], r, c))
                    visited[r][c] = True

        heapify(heap)
        water = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while heap:
            level, r, c = heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    height = heightMap[nr][nc]

                    water += max(0, level - height)
                    heappush(heap, (max(level, height), nr, nc))

        return water