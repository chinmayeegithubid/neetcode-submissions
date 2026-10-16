from collections import deque


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        operations = 0

        while queue:
            values = []

            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            target = {
                value: index
                for index, value in enumerate(sorted(values))
            }
            order = [target[value] for value in values]

            for i in range(len(order)):
                while order[i] != i:
                    j = order[i]
                    order[i], order[j] = order[j], order[i]
                    operations += 1

        return operations