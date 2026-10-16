from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = Counter()

        for word in words2:
            required |= Counter(word)

        result = []

        for word in words1:
            counts = Counter(word)

            if all(counts[char] >= count for char, count in required.items()):
                result.append(word)

        return result