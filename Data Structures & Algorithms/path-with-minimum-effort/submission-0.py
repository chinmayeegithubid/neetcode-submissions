import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            current, row, col = heapq.heappop(heap)

            if current > effort[row][col]:
                continue

            if row == rows - 1 and col == cols - 1:
                return current

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    difference = abs(heights[row][col] - heights[nr][nc])
                    next_effort = max(current, difference)

                    if next_effort < effort[nr][nc]:
                        effort[nr][nc] = next_effort
                        heapq.heappush(heap, (next_effort, nr, nc))