from collections import deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in graph}

        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            limit = min(len(first), len(second))

            if len(first) > len(second) and first[:limit] == second[:limit]:
                return ""

            for j in range(limit):
                a, b = first[j], second[j]

                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break

        queue = deque(char for char in indegree if indegree[char] == 0)
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(order) if len(order) == len(graph) else ""