class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 0:
                    continue

                stack = [(r, c)]
                grid2[r][c] = 0
                valid = True

                while stack:
                    row, col = stack.pop()

                    if grid1[row][col] == 0:
                        valid = False

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = row + dr, col + dc

                        if 0 <= nr < rows and 0 <= nc < cols and grid2[nr][nc] == 1:
                            grid2[nr][nc] = 0
                            stack.append((nr, nc))

                if valid:
                    result += 1

        return result