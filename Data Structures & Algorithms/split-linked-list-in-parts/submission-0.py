class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        base, extra = divmod(length, k)
        result = []
        current = head

        for i in range(k):
            result.append(current)
            size = base + (i < extra)

            if size == 0:
                continue

            for _ in range(size - 1):
                current = current.next

            following = current.next
            current.next = None
            current = following

        return result