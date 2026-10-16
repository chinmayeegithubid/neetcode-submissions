class Solution:
    def shortestPalindrome(self, s: str) -> str:
        combined = s + "#" + s[::-1]
        lps = [0] * len(combined)

        for i in range(1, len(combined)):
            length = lps[i - 1]

            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]

            if combined[i] == combined[length]:
                length += 1

            lps[i] = length

        prefix_length = lps[-1]
        return s[prefix_length:][::-1] + s