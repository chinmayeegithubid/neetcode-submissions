class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = [[] for _ in parent]
        self.owner = [0] * len(parent)

        for node, boss in enumerate(parent):
            if boss != -1:
                self.children[boss].append(node)

    def lock(self, num: int, user: int) -> bool:
        if self.owner[num] != 0:
            return False

        self.owner[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.owner[num] != user:
            return False

        self.owner[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        ancestor = num

        while ancestor != -1:
            if self.owner[ancestor] != 0:
                return False
            ancestor = self.parent[ancestor]

        locked = []
        stack = self.children[num].copy()

        while stack:
            node = stack.pop()

            if self.owner[node] != 0:
                locked.append(node)

            stack.extend(self.children[node])

        if not locked:
            return False

        for node in locked:
            self.owner[node] = 0

        self.owner[num] = user
        return True