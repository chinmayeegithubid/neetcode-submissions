from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        largest = -1

        for num, frequency in counts.items():
            if num == frequency:
                largest = max(largest, num)

        return largest