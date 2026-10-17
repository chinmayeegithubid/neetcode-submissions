class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent = {root.val: (None, "")}
        stack = [root]

        while startValue not in parent or destValue not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left.val] = (node.val, "L")
                stack.append(node.left)

            if node.right:
                parent[node.right.val] = (node.val, "R")
                stack.append(node.right)

        ancestors = {}
        value = startValue
        steps = 0

        while value is not None:
            ancestors[value] = steps
            value = parent[value][0]
            steps += 1

        downward = []
        value = destValue

        while value not in ancestors:
            value, direction = parent[value]
            downward.append(direction)

        return "U" * ancestors[value] + "".join(reversed(downward))