class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {char: i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]

            for a, b in zip(first, second):
                if a != b:
                    if rank[a] > rank[b]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False

        return True