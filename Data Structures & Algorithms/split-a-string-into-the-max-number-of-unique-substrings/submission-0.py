class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        used = set()
        best = 0
        n = len(s)

        def backtrack(start):
            nonlocal best

            if len(used) + n - start <= best:
                return

            if start == n:
                best = len(used)
                return

            for end in range(start + 1, n + 1):
                piece = s[start:end]

                if piece in used:
                    continue

                used.add(piece)
                backtrack(end)
                used.remove(piece)

        backtrack(0)
        return best