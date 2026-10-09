class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def sift_down(root: int, size: int) -> None:
            while 2 * root + 1 < size:
                child = 2 * root + 1

                if child + 1 < size and nums[child + 1] > nums[child]:
                    child += 1

                if nums[root] >= nums[child]:
                    break

                nums[root], nums[child] = nums[child], nums[root]
                root = child

        # Build a max-heap.
        for i in range(n // 2 - 1, -1, -1):
            sift_down(i, n)

        # Move the largest remaining element to its final position.
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            sift_down(0, end)

        return nums