class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        for i in nums:
            current = i
            length = 1
            if current - 1 not in s:
                while current + 1 in s:
                    current = current + 1
                    length = length + 1
            res = max(length, res)
        return res

        