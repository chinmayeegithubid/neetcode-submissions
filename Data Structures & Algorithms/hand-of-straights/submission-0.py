from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)

        for start in sorted(counts):
            frequency = counts[start]

            if frequency == 0:
                continue

            for value in range(start, start + groupSize):
                if counts[value] < frequency:
                    return False
                counts[value] -= frequency

        return True