from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        stack = []

        def mark(r, c):
            if board[r][c] == "O":
                board[r][c] = "#"
                stack.append((r, c))

        # Protect all border-connected regions
        for r in range(rows):
            mark(r, 0)
            mark(r, cols - 1)

        for c in range(cols):
            mark(0, c)
            mark(rows - 1, c)

        while stack:
            r, c = stack.pop()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    mark(nr, nc)

        # Capture surrounded regions and restore protected cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"