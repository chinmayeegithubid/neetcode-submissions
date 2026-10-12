class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(row: int, col: int, size: int) -> 'Node':
            if size == 1:
                return Node(bool(grid[row][col]), True,
                            None, None, None, None)

            half = size // 2
            top_left = build(row, col, half)
            top_right = build(row, col + half, half)
            bottom_left = build(row + half, col, half)
            bottom_right = build(row + half, col + half, half)

            if (
                top_left.isLeaf
                and top_right.isLeaf
                and bottom_left.isLeaf
                and bottom_right.isLeaf
                and top_left.val == top_right.val
                == bottom_left.val == bottom_right.val
            ):
                return Node(top_left.val, True, None, None, None, None)

            return Node(True, False, top_left, top_right,
                        bottom_left, bottom_right)

        return build(0, 0, len(grid))