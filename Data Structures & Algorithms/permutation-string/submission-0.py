class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)

        if size > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26

        for char in s1:
            target[ord(char) - ord('a')] += 1

        for right, char in enumerate(s2):
            window[ord(char) - ord('a')] += 1

            # Remove the character outside the fixed-size window.
            if right >= size:
                outgoing = s2[right - size]
                window[ord(outgoing) - ord('a')] -= 1

            if right >= size - 1 and window == target:
                return True

        return False