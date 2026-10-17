class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = {}
        result = 0

        for word in words:
            node = trie

            for i, char in enumerate(word):
                pair = (ord(char) - ord("a")) * 26 + (
                    ord(word[-1 - i]) - ord("a")
                )

                if pair not in node:
                    node[pair] = {"#": 0}

                node = node[pair]
                result += node["#"]

            node["#"] += 1

        return result