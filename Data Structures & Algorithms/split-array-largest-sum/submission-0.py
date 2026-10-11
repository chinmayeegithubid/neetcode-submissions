class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        while left < right:
            limit = (left + right) // 2
            groups = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > limit:
                    groups += 1
                    current_sum = 0
                current_sum += num

            if groups <= k:
                right = limit
            else:
                left = limit + 1

        return left