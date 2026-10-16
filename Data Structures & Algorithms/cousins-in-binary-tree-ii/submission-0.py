class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.val = 0
        level = [root]

        while level:
            next_level = []
            next_sum = 0

            for node in level:
                if node.left:
                    next_level.append(node.left)
                    next_sum += node.left.val
                if node.right:
                    next_level.append(node.right)
                    next_sum += node.right.val

            for node in level:
                sibling_sum = (
                    (node.left.val if node.left else 0)
                    + (node.right.val if node.right else 0)
                )

                if node.left:
                    node.left.val = next_sum - sibling_sum
                if node.right:
                    node.right.val = next_sum - sibling_sum

            level = next_level

        return root