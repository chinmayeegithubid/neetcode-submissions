class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return bool(root.val)

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        return self.evaluateTree(root.left) and self.evaluateTree(root.right)