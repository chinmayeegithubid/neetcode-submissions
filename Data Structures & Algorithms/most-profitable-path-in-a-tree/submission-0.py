class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Find each node's parent in the tree rooted at 0.
        parent = [-1] * n
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    stack.append(neighbor)

        # Bob visits only the nodes on his path to the root.
        bob_time = [n] * n
        node, time = bob, 0

        while node != -1:
            bob_time[node] = time
            node = parent[node]
            time += 1

        best = float("-inf")
        stack = [(0, 0, 0)]  # node, Alice's arrival time, income

        while stack:
            node, time, income = stack.pop()

            if time < bob_time[node]:
                income += amount[node]
            elif time == bob_time[node]:
                income += amount[node] // 2

            if node != 0 and len(graph[node]) == 1:
                best = max(best, income)
                continue

            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    stack.append((neighbor, time + 1, income))

        return best