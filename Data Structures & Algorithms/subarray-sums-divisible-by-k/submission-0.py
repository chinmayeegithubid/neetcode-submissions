class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = [0] * k
        counts[0] = 1
        remainder = 0
        result = 0

        for num in nums:
            remainder = (remainder + num) % k
            result += counts[remainder]
            counts[remainder] += 1

        return result