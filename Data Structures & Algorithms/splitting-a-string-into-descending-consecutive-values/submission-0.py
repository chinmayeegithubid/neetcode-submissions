class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def matches(start, expected):
            if start == n:
                return True

            if expected < 0:
                return False

            if expected == 0:
                return all(s[i] == "0" for i in range(start, n))

            value = 0

            for end in range(start, n):
                value = value * 10 + int(s[end])

                if value == expected:
                    return matches(end + 1, expected - 1)

                if value > expected:
                    return False

            return False

        first = 0

        for end in range(n - 1):
            first = first * 10 + int(s[end])

            if matches(end + 1, first - 1):
                return True

        return False