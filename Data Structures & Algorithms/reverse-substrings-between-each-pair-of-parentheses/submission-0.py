class Solution:
    def reverseParentheses(self, s: str) -> str:
        pairs = [0] * len(s)
        stack = []

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                opening = stack.pop()
                pairs[opening] = i
                pairs[i] = opening

        result = []
        i, direction = 0, 1

        while 0 <= i < len(s):
            if s[i] in "()":
                i = pairs[i]
                direction = -direction
            else:
                result.append(s[i])

            i += direction

        return "".join(result)