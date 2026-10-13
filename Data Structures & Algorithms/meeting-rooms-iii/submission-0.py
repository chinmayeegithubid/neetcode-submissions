import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = list(range(n))
        heapq.heapify(available)

        busy = []  # (finish_time, room_number)
        counts = [0] * n

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                finish = end
            else:
                free_time, room = heapq.heappop(busy)
                finish = free_time + (end - start)

            counts[room] += 1
            heapq.heappush(busy, (finish, room))

        return max(range(n), key=lambda room: counts[room])