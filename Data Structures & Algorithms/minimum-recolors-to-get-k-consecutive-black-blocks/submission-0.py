class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        minimum = k

        for i, block in enumerate(blocks):
            whites += block == "W"

            if i >= k:
                whites -= blocks[i - k] == "W"

            if i >= k - 1:
                minimum = min(minimum, whites)

        return minimum