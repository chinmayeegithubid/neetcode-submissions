from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for i in range(1, len(words)):
            common &= Counter(words[i])

        return list(common.elements())