class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        group = head.next

        while group:
            total = 0
            current = group

            while current.val != 0:
                total += current.val
                current = current.next

            group.val = total
            group.next = current.next
            group = group.next

        return head.next