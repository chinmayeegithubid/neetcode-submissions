from collections import deque
from heapq import heappush, heapreplace


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        queue = deque([root])
        largest = []

        while queue:
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if len(largest) < k:
                heappush(largest, level_sum)
            elif level_sum > largest[0]:
                heapreplace(largest, level_sum)

        return largest[0] if len(largest) == k else -1