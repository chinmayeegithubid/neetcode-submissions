class Solution:
    def numDecodings(self, s: str) -> int:
        previous = 1
        current = 1 if s[0] != "0" else 0

        for i in range(1, len(s)):
            ways = 0

            # Decode the current digit alone.
            if s[i] != "0":
                ways += current

            # Decode the previous and current digits together.
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                ways += previous

            previous, current = current, ways

        return current