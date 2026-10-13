from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = sum(count // 2 * 2 for count in counts.values())

        return length + (length < len(s))