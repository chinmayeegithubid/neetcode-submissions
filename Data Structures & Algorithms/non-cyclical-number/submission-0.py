class Solution:
    def isHappy(self, n: int) -> bool:
        def next_number(number: int) -> int:
            total = 0
            while number:
                number, digit = divmod(number, 10)
                total += digit * digit
            return total

        slow = n
        fast = next_number(n)

        while fast != 1 and slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        return fast == 1