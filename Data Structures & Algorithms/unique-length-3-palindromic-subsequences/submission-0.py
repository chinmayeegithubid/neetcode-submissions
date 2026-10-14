class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0

        for char in set(s):
            first = s.find(char)
            last = s.rfind(char)

            middle_chars = {
                s[i] for i in range(first + 1, last)
            }
            result += len(middle_chars)

        return result