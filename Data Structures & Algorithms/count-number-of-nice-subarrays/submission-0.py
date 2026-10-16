class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(limit):
            left = 0
            odd_count = 0
            count = 0

            for right, value in enumerate(nums):
                odd_count += value % 2

                while odd_count > limit:
                    odd_count -= nums[left] % 2
                    left += 1

                count += right - left + 1

            return count

        return at_most(k) - at_most(k - 1)