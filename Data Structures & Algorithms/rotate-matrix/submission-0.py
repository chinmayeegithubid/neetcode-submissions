from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Reverse the order of rows.
        matrix.reverse()

        # Transpose across the main diagonal.
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row], matrix[row][col]
                )