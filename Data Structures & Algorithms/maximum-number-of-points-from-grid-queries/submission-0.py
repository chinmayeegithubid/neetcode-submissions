from heapq import heappush, heappop

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        answer = [0] * len(queries)
        visited = [[False] * cols for _ in range(rows)]

        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        points = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for limit, index in sorted((q, i) for i, q in enumerate(queries)):
            while heap and heap[0][0] < limit:
                _, r, c = heappop(heap)
                points += 1

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heappush(heap, (grid[nr][nc], nr, nc))

            answer[index] = points

        return answer