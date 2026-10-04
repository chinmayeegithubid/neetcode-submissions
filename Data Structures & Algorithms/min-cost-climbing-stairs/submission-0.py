from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        previous, current = 0, 0

        for i in range(2, len(cost) + 1):
            next_cost = min(
                current + cost[i - 1],
                previous + cost[i - 2]
            )
            previous, current = current, next_cost

        return current