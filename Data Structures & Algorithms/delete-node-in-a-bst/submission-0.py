class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None
        node = root

        while node and node.val != key:
            parent = node
            node = node.left if key < node.val else node.right

        if node is None:
            return root

        if node.left and node.right:
            successor_parent = node
            successor = node.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            node.val = successor.val
            parent = successor_parent
            node = successor

        child = node.left if node.left else node.right

        if parent is None:
            return child

        if parent.left is node:
            parent.left = child
        else:
            parent.right = child

        return root