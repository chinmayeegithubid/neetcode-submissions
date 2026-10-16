class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = {char: s.count(char) for char in "abc"}

        if min(counts.values()) < k:
            return -1

        left = 0
        longest = 0

        for right, char in enumerate(s):
            counts[char] -= 1

            while counts[char] < k:
                counts[s[left]] += 1
                left += 1

            longest = max(longest, right - left + 1)

        return len(s) - longest