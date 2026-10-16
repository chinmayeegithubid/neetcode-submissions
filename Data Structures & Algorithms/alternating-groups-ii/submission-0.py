class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        streak = 1
        result = 0

        for i in range(1, n + k - 1):
            if colors[i % n] != colors[(i - 1) % n]:
                streak += 1
            else:
                streak = 1

            if streak >= k:
                result += 1

        return result