class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            result.append(chr(ord("A") + remainder))

        return "".join(reversed(result))