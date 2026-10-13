class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if len(matchsticks) < 4 or total % 4 != 0:
            return False

        target = total // 4
        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False

        sides = [0] * 4

        def backtrack(i: int) -> bool:
            if i == len(matchsticks):
                return True

            tried = set()

            for side in range(4):
                if sides[side] in tried:
                    continue
                tried.add(sides[side])

                if sides[side] + matchsticks[i] > target:
                    continue

                sides[side] += matchsticks[i]

                if backtrack(i + 1):
                    return True

                sides[side] -= matchsticks[i]

            return False

        return backtrack(0)