class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_deficit = 0

        for char in s:
            balance += 1 if char == "[" else -1
            max_deficit = max(max_deficit, -balance)

        return (max_deficit + 1) // 2