from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result = []
        combination = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(combination.copy())
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                combination.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                combination.pop()

        backtrack(0, target)
        return result