class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0

        def balance(node):
            nonlocal moves

            if not node:
                return 0

            left = balance(node.left)
            right = balance(node.right)

            moves += abs(left) + abs(right)

            return node.val + left + right - 1

        balance(root)
        return moves