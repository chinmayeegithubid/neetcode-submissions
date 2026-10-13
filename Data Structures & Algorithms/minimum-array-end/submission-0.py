class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        remaining = n - 1
        bit = 1

        while remaining:
            if (x & bit) == 0:
                if remaining & 1:
                    result |= bit
                remaining >>= 1

            bit <<= 1

        return result