from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)

        if "0000" in visited:
            return -1

        queue = deque([("0000", 0)])
        visited.add("0000")

        while queue:
            code, turns = queue.popleft()

            if code == target:
                return turns

            for i in range(4):
                digit = int(code[i])

                for direction in (-1, 1):
                    next_digit = str((digit + direction) % 10)
                    neighbor = code[:i] + next_digit + code[i + 1:]

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, turns + 1))

        return -1