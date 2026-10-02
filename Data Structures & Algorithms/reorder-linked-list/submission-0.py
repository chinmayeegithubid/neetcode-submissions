class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the end of the first half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split and reverse the second half
        current = slow.next
        slow.next = None
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # 3. Merge the halves alternately
        first, second = head, prev

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second