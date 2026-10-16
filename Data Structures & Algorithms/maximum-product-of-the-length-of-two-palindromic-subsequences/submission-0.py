class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        size = 1 << n
        palindrome = [0] * size

        for mask in range(1, size):
            subsequence = "".join(
                s[i] for i in range(n) if mask & (1 << i)
            )

            if subsequence == subsequence[::-1]:
                palindrome[mask] = len(subsequence)

        best = palindrome.copy()

        for i in range(n):
            bit = 1 << i

            for mask in range(size):
                if mask & bit:
                    best[mask] = max(best[mask], best[mask ^ bit])

        full_mask = size - 1
        result = 0

        for mask in range(1, size):
            result = max(
                result,
                palindrome[mask] * best[full_mask ^ mask]
            )

        return result