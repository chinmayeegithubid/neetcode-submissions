from bisect import bisect_right


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prices = []
        best_beauties = []
        best = 0

        for price, beauty in items:
            prices.append(price)
            best = max(best, beauty)
            best_beauties.append(best)

        result = []

        for budget in queries:
            index = bisect_right(prices, budget) - 1
            result.append(best_beauties[index] if index >= 0 else 0)

        return result