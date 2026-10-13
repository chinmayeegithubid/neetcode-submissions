from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)

        if max(counts.values()) > (len(s) + 1) // 2:
            return ""

        heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(heap)

        result = []
        previous_count, previous_char = 0, ""

        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)

            if previous_count < 0:
                heapq.heappush(heap, (previous_count, previous_char))

            previous_count, previous_char = count + 1, char

        return "".join(result)