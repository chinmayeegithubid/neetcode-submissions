from typing import List

class Solution:
    def maxNumEdgesToRemove(
        self, n: int, edges: List[List[int]]
    ) -> int:
        class DSU:
            def __init__(self):
                self.parent = list(range(n + 1))
                self.size = [1] * (n + 1)
                self.components = n

            def find(self, node):
                while node != self.parent[node]:
                    self.parent[node] = self.parent[self.parent[node]]
                    node = self.parent[node]
                return node

            def union(self, a, b):
                a, b = self.find(a), self.find(b)

                if a == b:
                    return False

                if self.size[a] < self.size[b]:
                    a, b = b, a

                self.parent[b] = a
                self.size[a] += self.size[b]
                self.components -= 1
                return True

        alice = DSU()
        bob = DSU()
        kept = 0

        # First, build connectivity using shared edges.
        for edge_type, u, v in edges:
            if edge_type == 3:
                merged_alice = alice.union(u, v)
                merged_bob = bob.union(u, v)

                if merged_alice or merged_bob:
                    kept += 1

        # Then add necessary exclusive edges.
        for edge_type, u, v in edges:
            if edge_type == 1:
                if alice.union(u, v):
                    kept += 1
            elif edge_type == 2:
                if bob.union(u, v):
                    kept += 1

        if alice.components != 1 or bob.components != 1:
            return -1

        return len(edges) - kept