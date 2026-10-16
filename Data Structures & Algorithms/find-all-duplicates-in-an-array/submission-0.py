class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            value = abs(num)
            index = value - 1

            if nums[index] < 0:
                result.append(value)
            else:
                nums[index] = -nums[index]

        return result