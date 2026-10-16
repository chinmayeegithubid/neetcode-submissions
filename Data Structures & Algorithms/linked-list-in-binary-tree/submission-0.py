class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def matches(list_node, tree_node):
            if not list_node:
                return True

            if not tree_node or list_node.val != tree_node.val:
                return False

            return (
                matches(list_node.next, tree_node.left)
                or matches(list_node.next, tree_node.right)
            )

        stack = [root] if root else []

        while stack:
            node = stack.pop()

            if matches(head, node):
                return True

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return False