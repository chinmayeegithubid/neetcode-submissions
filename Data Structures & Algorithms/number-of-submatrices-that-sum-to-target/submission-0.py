class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        result = 0

        for top in range(rows):
            column_sums = [0] * cols

            for bottom in range(top, rows):
                for col in range(cols):
                    column_sums[col] += matrix[bottom][col]

                counts = {0: 1}
                prefix = 0

                for value in column_sums:
                    prefix += value
                    result += counts.get(prefix - target, 0)
                    counts[prefix] = counts.get(prefix, 0) + 1

        return result