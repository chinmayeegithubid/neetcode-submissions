class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n

        for stronger, weaker in edges:
            indegree[weaker] += 1

        champion = -1

        for team in range(n):
            if indegree[team] == 0:
                if champion != -1:
                    return -1
                champion = team

        return champion