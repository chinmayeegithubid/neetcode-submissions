from itertools import zip_longest


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root):
            stack = [root] if root else []

            while stack:
                node = stack.pop()

                if not node.left and not node.right:
                    yield node.val
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)

        return all(
            first == second
            for first, second in zip_longest(leaves(root1), leaves(root2))
        )