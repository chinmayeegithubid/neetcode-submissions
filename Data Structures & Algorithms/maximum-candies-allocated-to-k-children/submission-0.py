class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = min(max(candies), sum(candies) // k)

        while left <= right:
            mid = (left + right) // 2
            children = 0

            for pile in candies:
                children += pile // mid
                if children >= k:
                    break

            if children >= k:
                left = mid + 1
            else:
                right = mid - 1

        return right