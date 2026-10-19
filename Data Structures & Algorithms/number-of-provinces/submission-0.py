class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for city in range(n):
            if visited[city]:
                continue

            provinces += 1
            stack = [city]
            visited[city] = True

            while stack:
                current = stack.pop()

                for neighbor, connected in enumerate(isConnected[current]):
                    if connected and not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

        return provinces