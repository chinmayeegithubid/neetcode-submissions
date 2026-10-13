from collections import deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]],
                    colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions):
            graph = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)

            for first, second in conditions:
                graph[first].append(second)
                indegree[second] += 1

            queue = deque(
                number for number in range(1, k + 1)
                if indegree[number] == 0
            )
            order = []

            while queue:
                number = queue.popleft()
                order.append(number)

                for neighbor in graph[number]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            return order if len(order) == k else []

        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)

        if not row_order or not col_order:
            return []

        col_position = {
            number: col for col, number in enumerate(col_order)
        }
        matrix = [[0] * k for _ in range(k)]

        for row, number in enumerate(row_order):
            matrix[row][col_position[number]] = number

        return matrix