class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        parts = []

        def backtrack(start):
            remaining = 4 - len(parts)
            digits_left = len(s) - start

            if not remaining <= digits_left <= 3 * remaining:
                return

            if remaining == 0:
                result.append(".".join(parts))
                return

            for length in range(1, 4):
                end = start + length
                if end > len(s):
                    break

                if length > 1 and s[start] == "0":
                    break

                segment = s[start:end]
                if int(segment) > 255:
                    break

                parts.append(segment)
                backtrack(end)
                parts.pop()

        backtrack(0)
        return result