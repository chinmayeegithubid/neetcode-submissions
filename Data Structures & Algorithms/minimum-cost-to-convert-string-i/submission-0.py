from typing import List

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:
        inf = float("inf")
        dist = [[inf] * 26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0

        # Keep the cheapest rule for each directed pair.
        for a, b, price in zip(original, changed, cost):
            u = ord(a) - ord("a")
            v = ord(b) - ord("a")
            dist[u][v] = min(dist[u][v], price)

        # Find the cheapest conversions, including chains.
        for k in range(26):
            for i in range(26):
                if dist[i][k] == inf:
                    continue

                for j in range(26):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

        total = 0

        for a, b in zip(source, target):
            if a == b:
                continue

            price = dist[ord(a) - ord("a")][ord(b) - ord("a")]

            if price == inf:
                return -1

            total += price

        return total