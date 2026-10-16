class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if modified:
                    return False

                modified = True

                if i == 1 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return True