class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def distances(start):
            distance = [-1] * n
            steps = 0

            while start != -1 and distance[start] == -1:
                distance[start] = steps
                start = edges[start]
                steps += 1

            return distance

        first = distances(node1)
        second = distances(node2)
        best_distance = float("inf")
        answer = -1

        for node in range(n):
            if first[node] == -1 or second[node] == -1:
                continue

            current = max(first[node], second[node])

            if current < best_distance:
                best_distance = current
                answer = node

        return answer