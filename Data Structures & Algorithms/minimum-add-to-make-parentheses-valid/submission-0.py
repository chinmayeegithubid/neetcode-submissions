class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unmatched_open = 0
        insertions = 0

        for char in s:
            if char == "(":
                unmatched_open += 1
            elif unmatched_open > 0:
                unmatched_open -= 1
            else:
                insertions += 1

        return insertions + unmatched_open