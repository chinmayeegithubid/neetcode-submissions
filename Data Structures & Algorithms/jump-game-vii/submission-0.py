class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        reachable = [False] * len(s)
        reachable[0] = True
        count = 0

        for i in range(1, len(s)):
            if i >= minJump:
                count += reachable[i - minJump]

            if i > maxJump:
                count -= reachable[i - maxJump - 1]

            reachable[i] = s[i] == "0" and count > 0

        return reachable[-1]