class MyHashSet:
    def __init__(self):
        self.bits = bytearray(125001)

    def add(self, key: int) -> None:
        self.bits[key // 8] |= 1 << (key % 8)

    def remove(self, key: int) -> None:
        self.bits[key // 8] &= ~(1 << (key % 8))

    def contains(self, key: int) -> bool:
        return bool(self.bits[key // 8] & (1 << (key % 8)))