class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        shorter = sentence1.split()
        longer = sentence2.split()

        if len(shorter) > len(longer):
            shorter, longer = longer, shorter

        left = 0

        while left < len(shorter) and shorter[left] == longer[left]:
            left += 1

        right = 0

        while (
            right < len(shorter) - left
            and shorter[-1 - right] == longer[-1 - right]
        ):
            right += 1

        return left + right == len(shorter)