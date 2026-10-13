class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        largest = second_largest = 0
        smallest = second_smallest = float("inf")

        for num in nums:
            if num >= largest:
                second_largest, largest = largest, num
            elif num > second_largest:
                second_largest = num

            if num <= smallest:
                second_smallest, smallest = smallest, num
            elif num < second_smallest:
                second_smallest = num

        return largest * second_largest - smallest * second_smallest