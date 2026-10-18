class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = [[] for _ in range(n)]

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        parent = [-1] * n
        order = [0]

        for city in order:
            for neighbor in graph[city]:
                if neighbor != parent[city]:
                    parent[neighbor] = city
                    order.append(neighbor)

        representatives = [1] * n
        fuel = 0

        for city in reversed(order):
            if city == 0:
                continue

            fuel += (representatives[city] + seats - 1) // seats
            representatives[parent[city]] += representatives[city]

        return fuel