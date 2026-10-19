class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        size = 3 * len(grid)
        blocked = [[0] * size for _ in range(size)]

        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                for offset in range(3):
                    if char == "/":
                        blocked[3 * r + offset][3 * c + 2 - offset] = 1
                    elif char == "\\":
                        blocked[3 * r + offset][3 * c + offset] = 1

        regions = 0

        for r in range(size):
            for c in range(size):
                if blocked[r][c]:
                    continue

                regions += 1
                stack = [(r, c)]
                blocked[r][c] = 1

                while stack:
                    row, col = stack.pop()

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = row + dr, col + dc

                        if (
                            0 <= nr < size
                            and 0 <= nc < size
                            and blocked[nr][nc] == 0
                        ):
                            blocked[nr][nc] = 1
                            stack.append((nr, nc))

        return regions