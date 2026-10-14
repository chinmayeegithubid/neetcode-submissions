class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        counts = [1, 0]
        parity = 0
        result = 0

        for num in arr:
            parity = (parity + num) % 2
            result = (result + counts[1 - parity]) % MOD
            counts[parity] += 1

        return result