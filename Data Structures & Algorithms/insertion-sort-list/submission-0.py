class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        last_sorted = head

        while last_sorted and last_sorted.next:
            current = last_sorted.next

            if current.val >= last_sorted.val:
                last_sorted = current
            else:
                previous = dummy

                while previous.next.val <= current.val:
                    previous = previous.next

                last_sorted.next = current.next
                current.next = previous.next
                previous.next = current

        return dummy.next