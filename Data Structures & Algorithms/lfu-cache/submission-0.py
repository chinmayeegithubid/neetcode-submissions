from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> (value, frequency)
        self.groups = defaultdict(OrderedDict)
        self.min_frequency = 0

    def _touch(self, key: int) -> None:
        value, frequency = self.cache[key]
        del self.groups[frequency][key]

        if not self.groups[frequency]:
            del self.groups[frequency]
            if self.min_frequency == frequency:
                self.min_frequency += 1

        frequency += 1
        self.cache[key] = (value, frequency)
        self.groups[frequency][key] = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self._touch(key)
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            _, frequency = self.cache[key]
            self.cache[key] = (value, frequency)
            self._touch(key)
            return

        if len(self.cache) == self.capacity:
            group = self.groups[self.min_frequency]
            removed_key, _ = group.popitem(last=False)
            del self.cache[removed_key]

            if not group:
                del self.groups[self.min_frequency]

        self.cache[key] = (value, 1)
        self.groups[1][key] = None
        self.min_frequency = 1