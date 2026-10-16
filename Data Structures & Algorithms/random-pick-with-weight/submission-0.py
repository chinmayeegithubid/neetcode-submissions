from bisect import bisect_left
from random import randint


class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0

        for weight in w:
            total += weight
            self.prefix.append(total)

        self.total = total

    def pickIndex(self) -> int:
        target = randint(1, self.total)
        return bisect_left(self.prefix, target)