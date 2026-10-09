class MyHashMap:
    def __init__(self):
        self.values = [-1] * 1_000_001

    def put(self, key: int, value: int) -> None:
        self.values[key] = value

    def get(self, key: int) -> int:
        return self.values[key]

    def remove(self, key: int) -> None:
        self.values[key] = -1