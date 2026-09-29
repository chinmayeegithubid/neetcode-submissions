from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        need = Counter(t)
        window = {}
        formed = 0
        required = len(need)

        left = 0
        best_start = 0
        best_length = float("inf")

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            # Shrink while all required counts are satisfied.
            while formed == required:
                length = right - left + 1

                if length < best_length:
                    best_start = left
                    best_length = length

                outgoing = s[left]
                window[outgoing] -= 1

                if outgoing in need and window[outgoing] < need[outgoing]:
                    formed -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]