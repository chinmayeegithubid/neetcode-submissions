from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        frequencies = Counter(s)

        largest_odd = max(
            count for count in frequencies.values() if count % 2 == 1
        )
        smallest_even = min(
            count for count in frequencies.values() if count % 2 == 0
        )

        return largest_odd - smallest_even