class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_boundary(find_first):
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    result = mid
                    if find_first:
                        right = mid - 1
                    else:
                        left = mid + 1

            return result

        return [find_boundary(True), find_boundary(False)]