class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        has_incoming = [False] * n

        for source, destination in edges:
            has_incoming[destination] = True

        return [node for node in range(n) if not has_incoming[node]]