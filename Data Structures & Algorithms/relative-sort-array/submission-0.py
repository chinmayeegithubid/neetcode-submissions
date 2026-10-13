class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = [0] * 1001

        for num in arr1:
            counts[num] += 1

        result = []

        for num in arr2:
            result.extend([num] * counts[num])
            counts[num] = 0

        for num in range(1001):
            result.extend([num] * counts[num])

        return result