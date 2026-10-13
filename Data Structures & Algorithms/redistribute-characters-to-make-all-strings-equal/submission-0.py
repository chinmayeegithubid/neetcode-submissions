from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = Counter()

        for word in words:
            counts.update(word)

        return all(count % len(words) == 0 for count in counts.values())