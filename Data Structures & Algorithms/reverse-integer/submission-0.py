class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0

        # Keep values negative to safely handle -2147483648.
        if x > 0:
            x = -x

        result = 0
        last_digit_limit = 8 if negative else 7

        while x:
            digit = -(x % -10)
            x = (x + digit) // 10

            # Check overflow before multiplying.
            if result < -214748364:
                return 0
            if result == -214748364 and digit > last_digit_limit:
                return 0

            result = result * 10 - digit

        return result if negative else -result