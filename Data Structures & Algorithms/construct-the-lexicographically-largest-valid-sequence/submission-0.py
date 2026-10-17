class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        sequence = [0] * size
        used = [False] * (n + 1)

        def backtrack(index):
            while index < size and sequence[index] != 0:
                index += 1

            if index == size:
                return True

            for value in range(n, 0, -1):
                if used[value]:
                    continue

                second = index if value == 1 else index + value

                if second >= size or sequence[second] != 0:
                    continue

                sequence[index] = sequence[second] = value
                used[value] = True

                if backtrack(index + 1):
                    return True

                sequence[index] = sequence[second] = 0
                used[value] = False

            return False

        backtrack(0)
        return sequence