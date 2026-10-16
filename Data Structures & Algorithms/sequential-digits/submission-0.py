class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []

        for length in range(len(str(low)), min(len(str(high)), 9) + 1):
            for start in range(10 - length):
                number = int(digits[start:start + length])

                if low <= number <= high:
                    result.append(number)

        return result