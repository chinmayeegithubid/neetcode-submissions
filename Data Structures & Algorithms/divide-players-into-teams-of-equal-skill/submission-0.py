from collections import Counter


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        teams = len(skill) // 2
        total = sum(skill)

        if total % teams != 0:
            return -1

        target = total // teams
        counts = Counter(skill)
        chemistry = 0

        for value in skill:
            if counts[value] == 0:
                continue

            counts[value] -= 1
            partner = target - value

            if counts[partner] == 0:
                return -1

            counts[partner] -= 1
            chemistry += value * partner

        return chemistry