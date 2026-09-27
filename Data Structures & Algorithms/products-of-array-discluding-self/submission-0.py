class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full = 1
        zero = 0
        for n in nums:
            if n!= 0:
               full = full * n
            else:
                zero += 1

        for i in range(len(nums)):
            if nums[i] !=0 and zero > 0:
                nums[i] = 0
            elif nums[i] != 0:
                nums[i] = full // nums[i]
            elif nums[i] == 0 and zero == 1:
                nums[i] = full
            elif nums[i] == 0 and zero > 1:
                nums[i] = 0


        return nums
        