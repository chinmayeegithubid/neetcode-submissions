from typing import List

class Solution:
    def findTheCity(
        self,
        n: int,
        edges: List[List[int]],
        distanceThreshold: int
    ) -> int:
        dist = [[float("inf")] * n for _ in range(n)]

        for city in range(n):
            dist[city][city] = 0

        for u, v, weight in edges:
            dist[u][v] = dist[v][u] = weight

        # Find all-pairs shortest distances.
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

        answer = -1
        fewest = n

        for city in range(n):
            count = sum(
                other != city
                and dist[city][other] <= distanceThreshold
                for other in range(n)
            )

            # Ascending labels: updating on ties picks the greatest.
            if count <= fewest:
                fewest = count
                answer = city

        return answer