class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        opponent = "W" if color == "B" else "B"

        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue

                r, c = rMove + dr, cMove + dc
                count = 0

                while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                    count += 1
                    r += dr
                    c += dc

                if (
                    count > 0
                    and 0 <= r < 8
                    and 0 <= c < 8
                    and board[r][c] == color
                ):
                    return True

        return False