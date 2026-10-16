from collections import deque


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        seen_gap = False

        while queue:
            node = queue.popleft()

            if node is None:
                seen_gap = True
            else:
                if seen_gap:
                    return False

                queue.append(node.left)
                queue.append(node.right)

        return True