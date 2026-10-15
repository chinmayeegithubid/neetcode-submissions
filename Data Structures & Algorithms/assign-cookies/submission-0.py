class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0

        for cookie in s:
            if child == len(g):
                break

            if cookie >= g[child]:
                child += 1

        return child