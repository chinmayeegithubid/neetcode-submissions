from bisect import bisect_left


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            minimum = (success + spell - 1) // spell
            index = bisect_left(potions, minimum)
            result.append(m - index)

        return result