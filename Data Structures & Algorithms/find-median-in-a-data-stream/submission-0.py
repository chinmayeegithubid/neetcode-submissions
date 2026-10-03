import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap using negative values
        self.large = []  # Min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # Move the largest of the lower half to the upper half
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Keep small equal in size or one element larger
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2