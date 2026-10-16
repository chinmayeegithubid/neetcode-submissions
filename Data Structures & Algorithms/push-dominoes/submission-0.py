class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        force = 0

        for i, char in enumerate(dominoes):
            if char == "R":
                force = n
            elif char == "L":
                force = 0
            else:
                force = max(0, force - 1)

            forces[i] = force

        force = 0

        for i in range(n - 1, -1, -1):
            if dominoes[i] == "L":
                force = n
            elif dominoes[i] == "R":
                force = 0
            else:
                force = max(0, force - 1)

            forces[i] -= force

        return "".join(
            "R" if force > 0 else "L" if force < 0 else "."
            for force in forces
        )