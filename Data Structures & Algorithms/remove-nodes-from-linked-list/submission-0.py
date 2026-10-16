class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            previous = None

            while node:
                following = node.next
                node.next = previous
                previous = node
                node = following

            return previous

        head = reverse(head)
        current = head

        while current and current.next:
            if current.next.val < current.val:
                current.next = current.next.next
            else:
                current = current.next

        return reverse(head)