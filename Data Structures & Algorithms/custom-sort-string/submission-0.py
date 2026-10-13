from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        result = []

        for char in order:
            result.append(char * counts[char])
            counts.pop(char, None)

        for char, count in counts.items():
            result.append(char * count)

        return "".join(result)