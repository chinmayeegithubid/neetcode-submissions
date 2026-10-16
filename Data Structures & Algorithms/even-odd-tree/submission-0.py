from collections import deque


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        even_level = True

        while queue:
            previous = float("-inf") if even_level else float("inf")

            for _ in range(len(queue)):
                node = queue.popleft()
                value = node.val

                if even_level:
                    if value % 2 == 0 or value <= previous:
                        return False
                else:
                    if value % 2 == 1 or value >= previous:
                        return False

                previous = value

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            even_level = not even_level

        return True