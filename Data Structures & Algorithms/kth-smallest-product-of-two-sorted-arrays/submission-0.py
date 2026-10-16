from bisect import bisect_left, bisect_right


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums2)

        def count_at_most(limit):
            count = 0

            for value in nums1:
                if value > 0:
                    count += bisect_right(nums2, limit // value)
                elif value < 0:
                    # Multiplying by a negative reverses the inequality.
                    threshold = -((-limit) // value)
                    count += m - bisect_left(nums2, threshold)
                elif limit >= 0:
                    count += m

                if count >= k:
                    return count

            return count

        corners = (
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1],
        )
        low, high = min(corners), max(corners)

        while low < high:
            mid = (low + high) // 2

            if count_at_most(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low