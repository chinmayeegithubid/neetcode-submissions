from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)

        return "".join(
            char * frequency
            for char, frequency in counts.most_common()
        )