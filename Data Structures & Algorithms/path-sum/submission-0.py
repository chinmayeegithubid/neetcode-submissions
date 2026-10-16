class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, total = stack.pop()

            if not node.left and not node.right and total == targetSum:
                return True

            if node.right:
                stack.append((node.right, total + node.right.val))
            if node.left:
                stack.append((node.left, total + node.left.val))

        return False