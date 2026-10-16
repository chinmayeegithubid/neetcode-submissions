class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def at_most(limit):
            left, right = 0, len(nums) - 1
            count = 0

            while left < right:
                if nums[left] + nums[right] <= limit:
                    count += right - left
                    left += 1
                else:
                    right -= 1

            return count

        return at_most(upper) - at_most(lower - 1)