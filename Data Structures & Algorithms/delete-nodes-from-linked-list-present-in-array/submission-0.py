class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove = set(nums)
        dummy = ListNode(0, head)
        current = dummy

        while current.next:
            if current.next.val in remove:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next