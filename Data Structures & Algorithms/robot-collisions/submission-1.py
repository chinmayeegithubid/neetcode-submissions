class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        order = sorted(range(len(positions)), key=positions.__getitem__)
        remaining = healths.copy()
        stack = []

        for i in order:
            if directions[i] == "R":
                stack.append(i)
                continue

            while stack and remaining[i] > 0:
                j = stack[-1]

                if remaining[j] < remaining[i]:
                    remaining[j] = 0
                    remaining[i] -= 1
                    stack.pop()
                elif remaining[j] > remaining[i]:
                    remaining[j] -= 1
                    remaining[i] = 0
                else:
                    remaining[j] = 0
                    remaining[i] = 0
                    stack.pop()

        return [health for health in remaining if health > 0]