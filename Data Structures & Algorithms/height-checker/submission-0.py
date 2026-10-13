class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = [0] * 101

        for height in heights:
            counts[height] += 1

        expected = 1
        mismatches = 0

        for height in heights:
            while counts[expected] == 0:
                expected += 1

            if height != expected:
                mismatches += 1

            counts[expected] -= 1

        return mismatches