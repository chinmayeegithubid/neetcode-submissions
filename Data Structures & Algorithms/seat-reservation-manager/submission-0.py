from heapq import heappush, heappop


class SeatManager:
    def __init__(self, n: int):
        self.next_seat = 1
        self.available = []

    def reserve(self) -> int:
        if self.available:
            return heappop(self.available)

        seat = self.next_seat
        self.next_seat += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.available, seatNumber)