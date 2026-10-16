class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse_pairs(left, right, odd):
            if not left:
                return

            if odd:
                left.val, right.val = right.val, left.val

            reverse_pairs(left.left, right.right, not odd)
            reverse_pairs(left.right, right.left, not odd)

        if root:
            reverse_pairs(root.left, root.right, True)

        return root