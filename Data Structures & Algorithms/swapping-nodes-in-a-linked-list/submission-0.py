class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head

        for _ in range(k - 1):
            first = first.next

        fast = first
        second = head

        while fast.next:
            fast = fast.next
            second = second.next

        first.val, second.val = second.val, first.val

        return head