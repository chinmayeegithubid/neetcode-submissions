from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequencies = sorted(Counter(arr).values())
        remaining = len(frequencies)

        for count in frequencies:
            if count > k:
                break

            k -= count
            remaining -= 1

        return remaining