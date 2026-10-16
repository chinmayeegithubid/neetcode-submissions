class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        def reverse(node):
            previous = None

            while node:
                following = node.next
                node.next = previous
                previous = node
                node = following

            return previous

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half = reverse(slow.next)
        left, right = head, second_half
        result = True

        while right:
            if left.val != right.val:
                result = False
                break

            left = left.next
            right = right.next

        slow.next = reverse(second_half)
        return result