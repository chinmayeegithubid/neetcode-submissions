class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        stack = [(root1, root2)]

        while stack:
            first, second = stack.pop()
            first.val += second.val

            if first.left and second.left:
                stack.append((first.left, second.left))
            elif second.left:
                first.left = second.left

            if first.right and second.right:
                stack.append((first.right, second.right))
            elif second.right:
                first.right = second.right

        return root1