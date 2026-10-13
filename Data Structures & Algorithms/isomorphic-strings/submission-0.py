class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward = {}
        backward = {}

        for a, b in zip(s, t):
            if a in forward and forward[a] != b:
                return False
            if b in backward and backward[b] != a:
                return False

            forward[a] = b
            backward[b] = a

        return True