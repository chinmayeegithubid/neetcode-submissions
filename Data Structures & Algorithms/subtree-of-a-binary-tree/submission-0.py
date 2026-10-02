class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(a, b):
            pairs = [(a, b)]

            while pairs:
                a, b = pairs.pop()

                if a is None and b is None:
                    continue
                if a is None or b is None or a.val != b.val:
                    return False

                pairs.append((a.left, b.left))
                pairs.append((a.right, b.right))

            return True

        if subRoot is None:
            return True

        stack = [root] if root else []

        while stack:
            node = stack.pop()

            if node.val == subRoot.val and same_tree(node, subRoot):
                return True

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False