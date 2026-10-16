class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def previous_valid(text, index):
            skip = 0

            while index >= 0:
                if text[index] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break

                index -= 1

            return index

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = previous_valid(s, i)
            j = previous_valid(t, j)

            if i < 0 or j < 0:
                return i == j

            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True