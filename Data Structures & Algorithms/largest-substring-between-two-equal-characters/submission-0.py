class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_seen = {}
        longest = -1

        for i, char in enumerate(s):
            if char in first_seen:
                longest = max(longest, i - first_seen[char] - 1)
            else:
                first_seen[char] = i

        return longest