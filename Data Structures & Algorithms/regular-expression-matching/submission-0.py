from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            matches = i < len(s) and (p[j] == s[i] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                return (
                    dfs(i, j + 2)              # Use zero occurrences.
                    or (matches and dfs(i + 1, j))  # Consume one; allow more.
                )

            return matches and dfs(i + 1, j + 1)

        return dfs(0, 0)