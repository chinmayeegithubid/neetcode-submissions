from collections import Counter
from typing import List

class CountSquares:
    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        result = 0

        for (x, y), frequency in self.points.items():
            # The opposite corner must form a non-zero square diagonal.
            if x == qx or abs(x - qx) != abs(y - qy):
                continue

            result += (
                frequency
                * self.points[(x, qy)]
                * self.points[(qx, y)]
            )

        return result