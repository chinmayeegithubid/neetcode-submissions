class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy = Node()
        self.tail = self.dummy
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.dummy.next
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == self.size:
            self.addAtTail(val)
            return

        previous = self.dummy
        for _ in range(index):
            previous = previous.next

        previous.next = Node(val, previous.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        previous = self.dummy
        for _ in range(index):
            previous = previous.next

        removed = previous.next
        previous.next = removed.next

        if removed is self.tail:
            self.tail = previous

        self.size -= 1