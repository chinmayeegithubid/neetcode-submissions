from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numbers = [str(num) for num in nums]

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        numbers.sort(key=cmp_to_key(compare))

        if numbers[0] == "0":
            return "0"

        return "".join(numbers)