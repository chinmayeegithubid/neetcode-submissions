class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}

        for word in words:
            node = trie

            for char in word:
                if char not in node:
                    node[char] = {"#": 0}

                node = node[char]
                node["#"] += 1

        result = []

        for word in words:
            node = trie
            score = 0

            for char in word:
                node = node[char]
                score += node["#"]

            result.append(score)

        return result