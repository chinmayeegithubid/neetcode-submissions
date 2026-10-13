from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        max_length = max(map(len, wordDict))
        n = len(s)

        @lru_cache(None)
        def backtrack(start: int) -> List[str]:
            if start == n:
                return [""]

            sentences = []

            for end in range(start + 1, min(n, start + max_length) + 1):
                word = s[start:end]

                if word not in words:
                    continue

                for suffix in backtrack(end):
                    sentences.append(word + " " + suffix if suffix else word)

            return sentences

        return backtrack(0)