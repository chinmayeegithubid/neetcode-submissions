class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack = []
        current = root
        previous = None
        minimum = float("inf")

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if previous is not None:
                minimum = min(minimum, current.val - previous)

            previous = current.val
            current = current.right

        return minimum