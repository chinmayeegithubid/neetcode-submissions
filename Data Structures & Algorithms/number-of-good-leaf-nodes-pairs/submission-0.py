class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        if not root or distance < 2:
            return 0

        stack = [(root, False)]
        leaf_counts = {}
        answer = 0

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
                continue

            counts = [0] * distance

            if not node.left and not node.right:
                counts[0] = 1
            else:
                left = leaf_counts.pop(node.left, [0] * distance)
                right = leaf_counts.pop(node.right, [0] * distance)

                for i in range(distance - 1):
                    for j in range(distance - i - 1):
                        answer += left[i] * right[j]

                for depth in range(1, distance):
                    counts[depth] = left[depth - 1] + right[depth - 1]

            leaf_counts[node] = counts

        return answer