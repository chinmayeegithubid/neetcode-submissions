from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clones[current].neighbors.append(clones[neighbor])

        return clones[node]