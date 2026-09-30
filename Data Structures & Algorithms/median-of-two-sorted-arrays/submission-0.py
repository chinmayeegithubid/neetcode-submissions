from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        half = (m + n + 1) // 2
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            a_left = A[i - 1] if i > 0 else float("-inf")
            a_right = A[i] if i < m else float("inf")
            b_left = B[j - 1] if j > 0 else float("-inf")
            b_right = B[j] if j < n else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if (m + n) % 2:
                    return float(max(a_left, b_left))

                return (max(a_left, b_left) +
                        min(a_right, b_right)) / 2

            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1