class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        smaller_sum = 0
        best = -1

        for side in nums:
            if smaller_sum > side:
                best = smaller_sum + side

            smaller_sum += side

        return best