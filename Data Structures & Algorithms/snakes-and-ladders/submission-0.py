from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        finish = n * n
        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            square, rolls = queue.popleft()

            if square == finish:
                return rolls

            for landing in range(square + 1, min(square + 6, finish) + 1):
                row_from_bottom, col = divmod(landing - 1, n)
                row = n - 1 - row_from_bottom

                if row_from_bottom % 2 == 1:
                    col = n - 1 - col

                destination = board[row][col]
                if destination == -1:
                    destination = landing

                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, rolls + 1))

        return -1