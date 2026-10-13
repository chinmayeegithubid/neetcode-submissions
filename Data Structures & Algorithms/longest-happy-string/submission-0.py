import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [
            (-count, char)
            for count, char in [(a, "a"), (b, "b"), (c, "c")]
            if count > 0
        ]
        heapq.heapify(heap)
        result = []

        while heap:
            count, char = heapq.heappop(heap)

            if len(result) >= 2 and result[-1] == result[-2] == char:
                if not heap:
                    break

                other_count, other_char = heapq.heappop(heap)
                result.append(other_char)
                other_count += 1

                if other_count < 0:
                    heapq.heappush(heap, (other_count, other_char))

                heapq.heappush(heap, (count, char))
            else:
                result.append(char)
                count += 1

                if count < 0:
                    heapq.heappush(heap, (count, char))

        return "".join(result)