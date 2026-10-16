class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        m = len(removable)
        removed_at = [m + 1] * len(s)

        for step, index in enumerate(removable, 1):
            removed_at[index] = step

        def can_remove(k):
            j = 0

            for i, char in enumerate(s):
                if removed_at[i] > k and char == p[j]:
                    j += 1

                    if j == len(p):
                        return True

            return False

        left, right = 0, m

        while left < right:
            mid = (left + right + 1) // 2

            if can_remove(mid):
                left = mid
            else:
                right = mid - 1

        return left