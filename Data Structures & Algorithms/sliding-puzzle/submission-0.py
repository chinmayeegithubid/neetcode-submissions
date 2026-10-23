from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = "".join(str(value) for row in board for value in row)
        target = "123450"

        neighbors = (
            (1, 3),
            (0, 2, 4),
            (1, 5),
            (0, 4),
            (1, 3, 5),
            (2, 4)
        )

        queue = deque([(start, start.index("0"), 0)])
        visited = {start}

        while queue:
            state, zero, moves = queue.popleft()

            if state == target:
                return moves

            for neighbor in neighbors[zero]:
                tiles = list(state)
                tiles[zero], tiles[neighbor] = tiles[neighbor], tiles[zero]
                next_state = "".join(tiles)

                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, neighbor, moves + 1))

        return -1