from collections import deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n

        for person in favorite:
            indegree[person] += 1

        # Longest incoming chain, including the employee itself.
        depth = [1] * n
        queue = deque(i for i in range(n) if indegree[i] == 0)

        # Remove non-cycle nodes and calculate chain lengths.
        while queue:
            person = queue.popleft()
            nxt = favorite[person]

            depth[nxt] = max(depth[nxt], depth[person] + 1)
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                queue.append(nxt)

        longest_cycle = 0
        pair_total = 0

        # Remaining nodes belong to cycles.
        for person in range(n):
            if indegree[person] == 0:
                continue

            current = person
            cycle_length = 0

            while indegree[current] > 0:
                indegree[current] = 0
                cycle_length += 1
                current = favorite[current]

            if cycle_length == 2:
                partner = favorite[person]
                pair_total += depth[person] + depth[partner]
            else:
                longest_cycle = max(longest_cycle, cycle_length)

        return max(longest_cycle, pair_total)