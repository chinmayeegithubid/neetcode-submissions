class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(node):
            previous = None

            while node:
                following = node.next
                node.next = previous
                previous = node
                node = following

            return previous

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = reverse(slow)
        left, right = head, second_half
        best = 0

        while right:
            best = max(best, left.val + right.val)
            left = left.next
            right = right.next

        reverse(second_half)
        return best