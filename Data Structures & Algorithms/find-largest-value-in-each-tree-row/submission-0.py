from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            largest = queue[0].val

            for _ in range(len(queue)):
                node = queue.popleft()
                largest = max(largest, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(largest)

        return result