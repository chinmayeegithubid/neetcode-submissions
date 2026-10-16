class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        stack = []

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                index = stack.pop()
                result[index] -= price

            stack.append(i)

        return result