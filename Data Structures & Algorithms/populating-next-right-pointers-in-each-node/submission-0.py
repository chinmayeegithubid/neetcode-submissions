class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftmost = root

        while leftmost.left:
            current = leftmost

            while current:
                current.left.next = current.right
                current.right.next = (
                    current.next.left if current.next else None
                )
                current = current.next

            leftmost = leftmost.left

        return root