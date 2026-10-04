from typing import List

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]],
        src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            next_prices = prices.copy()
            changed = False

            for source, destination, cost in flights:
                new_cost = prices[source] + cost

                if new_cost < next_prices[destination]:
                    next_prices[destination] = new_cost
                    changed = True

            prices = next_prices

            if not changed:
                break

        return prices[dst] if prices[dst] != float("inf") else -1