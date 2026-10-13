class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(start: int) -> None:
            if len(combination) == k:
                result.append(combination.copy())
                return

            needed = k - len(combination)

            for num in range(start, n - needed + 2):
                combination.append(num)
                backtrack(num + 1)
                combination.pop()

        backtrack(1)
        return result