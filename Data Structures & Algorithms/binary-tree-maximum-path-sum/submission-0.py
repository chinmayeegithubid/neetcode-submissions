class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")
        gains = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left = max(0, gains.get(node.left, 0))
                right = max(0, gains.get(node.right, 0))

                best = max(best, node.val + left + right)
                gains[node] = node.val + max(left, right)

        return best