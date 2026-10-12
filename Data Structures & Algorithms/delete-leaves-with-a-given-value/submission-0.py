class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode],
                        target: int) -> Optional[TreeNode]:
        if root is None:
            return None

        dummy = TreeNode(0)
        dummy.left = root
        stack = [(root, dummy, False)]

        while stack:
            node, parent, visited = stack.pop()

            if not visited:
                stack.append((node, parent, True))
                if node.right:
                    stack.append((node.right, node, False))
                if node.left:
                    stack.append((node.left, node, False))
            elif node.val == target and node.left is None and node.right is None:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None

        return dummy.left