from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = float("-inf")
        rest = 0

        for i in range(1, len(prices)):
            hold, sold, rest = (
                max(hold, rest - prices[i]),
                hold + prices[i],
                max(rest, sold)
            )

        return max(sold, rest)