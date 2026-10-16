class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            operations = 0

            for balls in nums:
                operations += (balls - 1) // mid
                if operations > maxOperations:
                    break

            if operations <= maxOperations:
                right = mid
            else:
                left = mid + 1

        return left