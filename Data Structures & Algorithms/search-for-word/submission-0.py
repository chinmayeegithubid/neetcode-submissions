from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        if len(word) > rows * cols:
            return False

        def dfs(r, c, i):
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or board[r][c] != word[i]):
                return False

            if i == len(word) - 1:
                return True

            char = board[r][c]
            board[r][c] = "#"  # Mark as visited

            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            board[r][c] = char  # Restore when backtracking
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False