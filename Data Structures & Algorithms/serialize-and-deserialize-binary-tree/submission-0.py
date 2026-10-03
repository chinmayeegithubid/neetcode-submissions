from collections import deque

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "N"

        values = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                values.append("N")
                continue

            values.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N":
            return None

        values = iter(data.split(","))
        root = TreeNode(int(next(values)))
        queue = deque([root])

        while queue:
            node = queue.popleft()

            left = next(values)
            if left != "N":
                node.left = TreeNode(int(left))
                queue.append(node.left)

            right = next(values)
            if right != "N":
                node.right = TreeNode(int(right))
                queue.append(node.right)

        return root