class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        head = None
        carry = 0

        while stack1 or stack2 or carry:
            total = carry

            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()

            carry, digit = divmod(total, 10)
            head = ListNode(digit, head)

        return head