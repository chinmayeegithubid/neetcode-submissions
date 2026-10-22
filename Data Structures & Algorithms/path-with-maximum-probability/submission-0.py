from heapq import heappush, heappop

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]

        for (u, v), probability in zip(edges, succProb):
            graph[u].append((v, probability))
            graph[v].append((u, probability))

        best = [0.0] * n
        best[start_node] = 1.0
        heap = [(-1.0, start_node)]

        while heap:
            negative_probability, node = heappop(heap)
            probability = -negative_probability

            if probability < best[node]:
                continue

            if node == end_node:
                return probability

            for neighbor, edge_probability in graph[node]:
                candidate = probability * edge_probability

                if candidate > best[neighbor]:
                    best[neighbor] = candidate
                    heappush(heap, (-candidate, neighbor))

        return 0.0