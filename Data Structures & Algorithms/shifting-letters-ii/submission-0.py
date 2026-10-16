class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        difference = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            change = 1 if direction == 1 else -1
            difference[start] += change
            difference[end + 1] -= change

        result = []
        shift = 0
        base = ord("a")

        for i, char in enumerate(s):
            shift += difference[i]
            result.append(chr(base + (ord(char) - base + shift) % 26))

        return "".join(result)