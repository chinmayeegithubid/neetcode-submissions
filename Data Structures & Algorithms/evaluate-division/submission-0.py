from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def evaluate(start: str, end: str) -> float:
            if start not in graph or end not in graph:
                return -1.0

            queue = deque([(start, 1.0)])
            visited = {start}

            while queue:
                variable, product = queue.popleft()

                if variable == end:
                    return product

                for neighbor, ratio in graph[variable]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * ratio))

            return -1.0

        return [evaluate(a, b) for a, b in queries]