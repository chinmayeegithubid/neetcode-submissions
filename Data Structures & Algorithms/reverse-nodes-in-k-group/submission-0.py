class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Check that a complete group of k nodes exists
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_next = kth.next

            # Reverse the current group
            prev = group_next
            current = group_prev.next

            while current is not group_next:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # Reconnect and advance to the next group
            group_tail = group_prev.next
            group_prev.next = kth
            group_prev = group_tail