from heapq import heappush, heappop


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        speed_sum = 0
        best = 0

        for current_efficiency, current_speed in engineers:
            heappush(heap, current_speed)
            speed_sum += current_speed

            if len(heap) > k:
                speed_sum -= heappop(heap)

            best = max(best, speed_sum * current_efficiency)

        return best % (10**9 + 7)