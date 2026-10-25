from collections import deque
from typing import List

class Solution:
    def largestPathValue(
        self, colors: str, edges: List[List[int]]
    ) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        color_ids = [ord(ch) - ord('a') for ch in colors]

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # dp[u][c]: maximum occurrences of color c
        # along any path ending at node u.
        dp = [[0] * 26 for _ in range(n)]

        for u in range(n):
            dp[u][color_ids[u]] = 1

        queue = deque(
            u for u in range(n) if indegree[u] == 0
        )

        answer = 0
        processed = 0

        while queue:
            u = queue.popleft()
            processed += 1
            current = dp[u]

            answer = max(answer, max(current))

            for v in graph[u]:
                next_counts = dp[v]
                next_color = color_ids[v]

                for c in range(26):
                    count = current[c] + (c == next_color)
                    if count > next_counts[c]:
                        next_counts[c] = count

                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return answer if processed == n else -1