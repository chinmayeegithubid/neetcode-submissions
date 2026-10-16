class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        stack = [(root, False)]
        path = []
        best = None

        while stack:
            node, exiting = stack.pop()

            if exiting:
                path.pop()
                continue

            path.append(chr(ord("a") + node.val))
            stack.append((node, True))

            if not node.left and not node.right:
                candidate = "".join(reversed(path))
                if best is None or candidate < best:
                    best = candidate
            else:
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return best