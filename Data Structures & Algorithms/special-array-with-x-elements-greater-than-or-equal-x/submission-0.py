class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        counts = [0] * (n + 1)

        for num in nums:
            counts[min(num, n)] += 1

        greater_or_equal = 0

        for x in range(n, 0, -1):
            greater_or_equal += counts[x]
            if greater_or_equal == x:
                return x

        return -1