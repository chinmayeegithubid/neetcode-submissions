class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n + 1)

        for person, trusted in trust:
            score[person] -= 1
            score[trusted] += 1

        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person

        return -1