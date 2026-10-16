class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        positive, negative = 0, 1

        for num in nums:
            if num > 0:
                result[positive] = num
                positive += 2
            else:
                result[negative] = num
                negative += 2

        return result