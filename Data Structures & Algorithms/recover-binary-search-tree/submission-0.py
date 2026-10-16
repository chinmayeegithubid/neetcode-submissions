class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = previous = None
        current = root

        while current:
            if current.left:
                predecessor = current.left

                while predecessor.right and predecessor.right is not current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                    continue

                predecessor.right = None

            if previous and previous.val > current.val:
                if first is None:
                    first = previous
                second = current

            previous = current
            current = current.right

        if first and second:
            first.val, second.val = second.val, first.val