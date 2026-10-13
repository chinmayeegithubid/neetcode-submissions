class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = len(grid) ** 2
        total = squared_total = 0

        for row in grid:
            for value in row:
                total += value
                squared_total += value * value

        difference = total - count * (count + 1) // 2
        squared_difference = (
            squared_total - count * (count + 1) * (2 * count + 1) // 6
        )

        combined = squared_difference // difference
        repeated = (combined + difference) // 2
        missing = (combined - difference) // 2

        return [repeated, missing]