class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {"a": -1, "b": -1, "c": -1}
        result = 0

        for i, char in enumerate(s):
            last_seen[char] = i
            result += min(last_seen.values()) + 1

        return result