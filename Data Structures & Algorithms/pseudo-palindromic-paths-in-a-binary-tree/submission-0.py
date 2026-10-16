class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)] if root else []
        result = 0

        while stack:
            node, mask = stack.pop()
            mask ^= 1 << node.val

            if not node.left and not node.right:
                if mask & (mask - 1) == 0:
                    result += 1
            else:
                if node.right:
                    stack.append((node.right, mask))
                if node.left:
                    stack.append((node.left, mask))

        return result