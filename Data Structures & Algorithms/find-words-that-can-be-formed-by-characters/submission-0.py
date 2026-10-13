from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        available = Counter(chars)
        total = 0

        for word in words:
            needed = Counter(word)

            if all(count <= available[char] for char, count in needed.items()):
                total += len(word)

        return total