class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            tail.next = l1 if l1 else l2
            return dummy.next

        interval = 1
        k = len(lists)

        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]