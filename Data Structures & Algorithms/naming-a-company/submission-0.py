class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = [set() for _ in range(26)]

        for idea in ideas:
            groups[ord(idea[0]) - ord("a")].add(idea[1:])

        result = 0

        for i in range(26):
            for j in range(i + 1, 26):
                common = len(groups[i] & groups[j])
                unique_i = len(groups[i]) - common
                unique_j = len(groups[j]) - common

                result += 2 * unique_i * unique_j

        return result