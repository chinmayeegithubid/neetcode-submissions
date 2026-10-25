from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:

        @lru_cache(None)
        def solve(oranges: int) -> int:
            if oranges <= 1:
                return oranges

            return 1 + min(
                oranges % 2 + solve(oranges // 2),
                oranges % 3 + solve(oranges // 3)
            )

        return solve(n)