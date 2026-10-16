class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed = 1 << k

        if len(s) - k + 1 < needed:
            return False

        seen = bytearray(needed)
        mask = needed - 1
        code = 0

        for i, char in enumerate(s):
            code = ((code << 1) & mask) | (char == "1")

            if i >= k - 1 and not seen[code]:
                seen[code] = 1
                needed -= 1

                if needed == 0:
                    return True

        return False