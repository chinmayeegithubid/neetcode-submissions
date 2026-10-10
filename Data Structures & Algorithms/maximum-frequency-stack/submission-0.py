from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.frequency = defaultdict(int)
        self.groups = defaultdict(list)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        freq = self.frequency[val]

        self.groups[freq].append(val)
        self.max_frequency = max(self.max_frequency, freq)

    def pop(self) -> int:
        val = self.groups[self.max_frequency].pop()
        self.frequency[val] -= 1

        if not self.groups[self.max_frequency]:
            del self.groups[self.max_frequency]
            self.max_frequency -= 1

        return val