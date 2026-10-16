from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 0)])
        widest = 0

        while queue:
            widest = max(widest, queue[-1][1] - queue[0][1] + 1)
            offset = queue[0][1]

            for _ in range(len(queue)):
                node, index = queue.popleft()
                index -= offset

                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

        return widest