from math import gcd


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = head

        while current and current.next:
            next_node = current.next
            current.next = ListNode(
                gcd(current.val, next_node.val), next_node
            )
            current = next_node

        return head