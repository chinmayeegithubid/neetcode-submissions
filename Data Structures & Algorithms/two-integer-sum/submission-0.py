class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate (nums):
            for j,m in enumerate(nums):
                if i != j and n + m == target:
                    return [i,j]
        