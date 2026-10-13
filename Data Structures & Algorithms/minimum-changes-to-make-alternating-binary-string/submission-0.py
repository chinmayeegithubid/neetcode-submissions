class Solution:
    def minOperations(self, s: str) -> int:
        changes = 0

        for i, char in enumerate(s):
            expected = "0" if i % 2 == 0 else "1"
            if char != expected:
                changes += 1

        return min(changes, len(s) - changes)