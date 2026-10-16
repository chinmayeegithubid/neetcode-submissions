class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []

        for num in nums:
            if num < pivot:
                result.append(num)

        for num in nums:
            if num == pivot:
                result.append(num)

        for num in nums:
            if num > pivot:
                result.append(num)

        return result