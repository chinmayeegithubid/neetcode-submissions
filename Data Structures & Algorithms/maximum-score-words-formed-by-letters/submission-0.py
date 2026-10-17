from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        available = Counter(letters)
        word_info = [
            (
                Counter(word),
                sum(score[ord(char) - ord("a")] for char in word),
            )
            for word in words
        ]

        def backtrack(index):
            if index == len(words):
                return 0

            best = backtrack(index + 1)
            needed, value = word_info[index]

            if all(available[char] >= count for char, count in needed.items()):
                for char, count in needed.items():
                    available[char] -= count

                best = max(best, value + backtrack(index + 1))

                for char, count in needed.items():
                    available[char] += count

            return best

        return backtrack(0)