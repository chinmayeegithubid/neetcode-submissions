class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        needed = sum(nums) % p
        if needed == 0:
            return 0

        latest = {0: -1}
        remainder = 0
        shortest = len(nums)

        for i, num in enumerate(nums):
            remainder = (remainder + num) % p
            target = (remainder - needed) % p

            if target in latest:
                shortest = min(shortest, i - latest[target])

            latest[remainder] = i

        return shortest if shortest < len(nums) else -1