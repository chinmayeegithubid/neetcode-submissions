class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)

        while left < right:
            mid = (left + right) // 2
            stores = 0

            for quantity in quantities:
                stores += (quantity + mid - 1) // mid
                if stores > n:
                    break

            if stores <= n:
                right = mid
            else:
                left = mid + 1

        return left