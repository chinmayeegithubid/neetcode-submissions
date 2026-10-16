class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        previous = head
        current = head.next
        position = 1
        first = last = -1
        minimum = float("inf")

        while current.next:
            is_peak = current.val > previous.val and current.val > current.next.val
            is_valley = current.val < previous.val and current.val < current.next.val

            if is_peak or is_valley:
                if first == -1:
                    first = position
                else:
                    minimum = min(minimum, position - last)

                last = position

            previous = current
            current = current.next
            position += 1

        if first == last:
            return [-1, -1]

        return [minimum, last - first]