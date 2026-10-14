from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)
        most_aligned = 0

        for row in wall:
            position = 0

            for i in range(len(row) - 1):
                position += row[i]
                edges[position] += 1
                most_aligned = max(most_aligned, edges[position])

        return len(wall) - most_aligned