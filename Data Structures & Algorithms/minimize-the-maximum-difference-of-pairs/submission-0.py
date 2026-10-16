class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            pairs = 0
            i = 0

            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= mid:
                    pairs += 1
                    i += 2
                else:
                    i += 1

                if pairs >= p:
                    break

            if pairs >= p:
                right = mid
            else:
                left = mid + 1

        return left