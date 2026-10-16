class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = [0] * (len(nums) + 1)
        result = []

        for num in nums:
            row = counts[num]

            if row == len(result):
                result.append([])

            result[row].append(num)
            counts[num] += 1

        return result