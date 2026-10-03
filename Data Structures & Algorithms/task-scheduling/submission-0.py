from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(freq == max_freq for freq in counts.values())

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + max_count
        )