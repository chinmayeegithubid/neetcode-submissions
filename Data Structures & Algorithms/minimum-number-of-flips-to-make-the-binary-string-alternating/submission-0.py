class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        mismatches = 0
        best = n

        for right in range(2 * n - 1):
            expected = "0" if right % 2 == 0 else "1"
            mismatches += s[right % n] != expected

            if right >= n:
                left = right - n
                expected_left = "0" if left % 2 == 0 else "1"
                mismatches -= s[left % n] != expected_left

            if right >= n - 1:
                best = min(best, mismatches, n - mismatches)

        return best