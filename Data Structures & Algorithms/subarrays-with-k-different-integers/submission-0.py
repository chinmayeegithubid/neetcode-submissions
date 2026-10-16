class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(limit):
            counts = {}
            left = 0
            result = 0

            for right, value in enumerate(nums):
                counts[value] = counts.get(value, 0) + 1

                while len(counts) > limit:
                    outgoing = nums[left]
                    counts[outgoing] -= 1

                    if counts[outgoing] == 0:
                        del counts[outgoing]

                    left += 1

                result += right - left + 1

            return result

        return at_most(k) - at_most(k - 1)