class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counts = {}
        bad_pairs = 0

        for i, value in enumerate(nums):
            key = value - i
            good_pairs = counts.get(key, 0)

            bad_pairs += i - good_pairs
            counts[key] = good_pairs + 1

        return bad_pairs