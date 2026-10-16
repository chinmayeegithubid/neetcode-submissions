from collections import Counter
from math import isqrt


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        counts = Counter(ranks)
        left, right = 0, min(counts) * cars * cars

        while left < right:
            mid = (left + right) // 2
            repaired = 0

            for rank, count in counts.items():
                repaired += count * isqrt(mid // rank)
                if repaired >= cars:
                    break

            if repaired >= cars:
                right = mid
            else:
                left = mid + 1

        return left