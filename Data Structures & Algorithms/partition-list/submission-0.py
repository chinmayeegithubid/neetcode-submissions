class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_dummy = ListNode()
        larger_dummy = ListNode()
        smaller = smaller_dummy
        larger = larger_dummy

        while head:
            if head.val < x:
                smaller.next = head
                smaller = head
            else:
                larger.next = head
                larger = head

            head = head.next

        larger.next = None
        smaller.next = larger_dummy.next

        return smaller_dummy.next