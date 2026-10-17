from bisect import bisect_left, bisect_right


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(start for start, end in flowers)
        ends = sorted(end for start, end in flowers)

        return [
            bisect_right(starts, time) - bisect_left(ends, time)
            for time in people
        ]