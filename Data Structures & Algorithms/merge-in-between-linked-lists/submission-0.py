class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        before = list1

        for _ in range(a - 1):
            before = before.next

        after = before.next

        for _ in range(b - a + 1):
            after = after.next

        tail = list2
        while tail.next:
            tail = tail.next

        before.next = list2
        tail.next = after

        return list1