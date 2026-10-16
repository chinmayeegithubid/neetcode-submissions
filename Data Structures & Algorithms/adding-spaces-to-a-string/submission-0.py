class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        parts = []
        start = 0

        for index in spaces:
            parts.append(s[start:index])
            start = index

        parts.append(s[start:])
        return " ".join(parts)