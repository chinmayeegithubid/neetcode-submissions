class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = sum(s[i] in vowels for i in range(k))
        best = count

        for i in range(k, len(s)):
            count += s[i] in vowels
            count -= s[i - k] in vowels
            best = max(best, count)

        return best