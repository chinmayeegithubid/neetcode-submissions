class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and not (low <= root.val <= high):
            root = root.right if root.val < low else root.left

        if not root:
            return None

        current = root
        while current:
            while current.left and current.left.val < low:
                current.left = current.left.right
            current = current.left

        current = root
        while current:
            while current.right and current.right.val > high:
                current.right = current.right.left
            current = current.right

        return root