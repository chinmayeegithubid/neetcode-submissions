class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deleted_values = set(to_delete)
        forest = []
        stack = [(root, True)] if root else []

        while stack:
            node, is_root = stack.pop()
            deleted = node.val in deleted_values

            if is_root and not deleted:
                forest.append(node)

            if node.left:
                stack.append((node.left, deleted))
                if node.left.val in deleted_values:
                    node.left = None

            if node.right:
                stack.append((node.right, deleted))
                if node.right.val in deleted_values:
                    node.right = None

        return forest