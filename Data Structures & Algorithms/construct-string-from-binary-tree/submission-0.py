class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        parts = []
        stack = [root]

        while stack:
            item = stack.pop()

            if isinstance(item, str):
                parts.append(item)
                continue

            parts.append(str(item.val))

            if item.right:
                stack.extend([")", item.right, "("])

            if item.left:
                stack.extend([")", item.left, "("])
            elif item.right:
                parts.append("()")

        return "".join(parts)