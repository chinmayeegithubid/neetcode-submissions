from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        available = Counter(magazine)

        for char in ransomNote:
            if available[char] == 0:
                return False
            available[char] -= 1

        return True