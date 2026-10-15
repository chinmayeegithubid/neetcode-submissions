class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        first_seen = {0: -1}
        remainder = 0

        for i, num in enumerate(nums):
            remainder = (remainder + num) % k

            if remainder in first_seen:
                if i - first_seen[remainder] >= 2:
                    return True
            else:
                first_seen[remainder] = i

        return False