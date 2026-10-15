class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                if read != write:
                    nums[write] = nums[read]
                    nums[read] = 0
                write += 1