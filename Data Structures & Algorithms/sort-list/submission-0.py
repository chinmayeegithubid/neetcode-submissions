class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        def split(node, size):
            if not node:
                return None

            for _ in range(size - 1):
                if not node.next:
                    break
                node = node.next

            following = node.next
            node.next = None
            return following

        dummy = ListNode(0, head)
        size = 1

        while size < length:
            previous = dummy
            current = dummy.next

            while current:
                left = current
                right = split(left, size)
                current = split(right, size)

                while left and right:
                    if left.val <= right.val:
                        previous.next = left
                        left = left.next
                    else:
                        previous.next = right
                        right = right.next

                    previous = previous.next

                previous.next = left if left else right

                while previous.next:
                    previous = previous.next

            size *= 2

        return dummy.next