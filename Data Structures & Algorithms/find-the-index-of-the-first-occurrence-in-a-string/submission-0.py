class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        lps = [0] * len(needle)
        j = 0

        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]

            if needle[i] == needle[j]:
                j += 1

            lps[i] = j

        j = 0

        for i, char in enumerate(haystack):
            while j > 0 and char != needle[j]:
                j = lps[j - 1]

            if char == needle[j]:
                j += 1

            if j == len(needle):
                return i - len(needle) + 1

        return -1