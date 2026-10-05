from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                end = i + len(word)

                if end <= n and dp[end] and s.startswith(word, i):
                    dp[i] = True
                    break

        return dp[0]