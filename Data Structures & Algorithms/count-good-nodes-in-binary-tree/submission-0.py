class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        stack = [(root, root.val)]

        while stack:
            node, path_max = stack.pop()

            if node.val >= path_max:
                count += 1

            path_max = max(path_max, node.val)

            if node.right:
                stack.append((node.right, path_max))
            if node.left:
                stack.append((node.left, path_max))

        return count