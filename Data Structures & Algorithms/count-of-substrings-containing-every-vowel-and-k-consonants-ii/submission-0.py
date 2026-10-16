class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")

        def at_least(limit):
            counts = {}
            consonants = 0
            left = 0
            result = 0

            for char in word:
                if char in vowels:
                    counts[char] = counts.get(char, 0) + 1
                else:
                    consonants += 1

                while len(counts) == 5 and consonants >= limit:
                    outgoing = word[left]

                    if outgoing in vowels:
                        counts[outgoing] -= 1
                        if counts[outgoing] == 0:
                            del counts[outgoing]
                    else:
                        consonants -= 1

                    left += 1

                result += left

            return result

        return at_least(k) - at_least(k + 1)