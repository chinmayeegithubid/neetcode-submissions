class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.capacity = k
        self.head = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        index = (self.head + self.size) % self.capacity
        self.data[index] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        index = (self.head + self.size - 1) % self.capacity
        return self.data[index]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity