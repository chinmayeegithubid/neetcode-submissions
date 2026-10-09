class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_positive = 0x7FFFFFFF

        a &= mask
        b &= mask

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= max_positive else ~(a ^ mask)