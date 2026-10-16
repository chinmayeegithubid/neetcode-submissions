from collections import defaultdict
from math import gcd


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counts = defaultdict(int)
        pairs = 0

        for width, height in rectangles:
            divisor = gcd(width, height)
            ratio = (width // divisor, height // divisor)

            pairs += counts[ratio]
            counts[ratio] += 1

        return pairs