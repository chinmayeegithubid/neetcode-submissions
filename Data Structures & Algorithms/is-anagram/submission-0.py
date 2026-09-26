class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26

        for i in s:
            chars[ord(i) - ord('a')] += 1

        for i in t:
            chars[ord(i) - ord('a')] -= 1

        for count in chars:
            if count != 0:
                return False

        return True