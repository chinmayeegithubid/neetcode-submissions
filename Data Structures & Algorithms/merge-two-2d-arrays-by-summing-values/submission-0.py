class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            id1, value1 = nums1[i]
            id2, value2 = nums2[j]

            if id1 == id2:
                result.append([id1, value1 + value2])
                i += 1
                j += 1
            elif id1 < id2:
                result.append([id1, value1])
                i += 1
            else:
                result.append([id2, value2])
                j += 1

        while i < len(nums1):
            result.append(nums1[i].copy())
            i += 1

        while j < len(nums2):
            result.append(nums2[j].copy())
            j += 1

        return result