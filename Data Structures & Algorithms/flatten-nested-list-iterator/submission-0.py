class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = [iter(nestedList)]
        self.next_value = None

    def next(self) -> int:
        self.hasNext()
        value = self.next_value
        self.next_value = None
        return value

    def hasNext(self) -> bool:
        if self.next_value is not None:
            return True

        while self.stack:
            try:
                item = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue

            if item.isInteger():
                self.next_value = item.getInteger()
                return True

            self.stack.append(iter(item.getList()))

        return False