from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = Counter(tiles)

        def backtrack():
            total = 0

            for letter in counts:
                if counts[letter] == 0:
                    continue

                counts[letter] -= 1
                total += 1 + backtrack()
                counts[letter] += 1

            return total

        return backtrack()