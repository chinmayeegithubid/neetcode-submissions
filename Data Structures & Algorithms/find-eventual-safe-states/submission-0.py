from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse = [[] for _ in range(n)]
        outgoing = [len(neighbors) for neighbors in graph]

        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse[neighbor].append(node)

        queue = deque(node for node in range(n) if outgoing[node] == 0)

        while queue:
            node = queue.popleft()

            for predecessor in reverse[node]:
                outgoing[predecessor] -= 1

                if outgoing[predecessor] == 0:
                    queue.append(predecessor)

        return [node for node in range(n) if outgoing[node] == 0]