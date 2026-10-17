class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        current = root
        total = 0

        while current or stack:
            while current:
                stack.append(current)
                current = current.right

            current = stack.pop()
            total += current.val
            current.val = total
            current = current.left

        return root