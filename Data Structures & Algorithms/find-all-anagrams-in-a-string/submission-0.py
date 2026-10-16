class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)

        if k > len(s):
            return []

        target = [0] * 26
        window = [0] * 26
        result = []

        for char in p:
            target[ord(char) - ord("a")] += 1

        for right, char in enumerate(s):
            window[ord(char) - ord("a")] += 1

            if right >= k:
                window[ord(s[right - k]) - ord("a")] -= 1

            if right >= k - 1 and window == target:
                result.append(right - k + 1)

        return result