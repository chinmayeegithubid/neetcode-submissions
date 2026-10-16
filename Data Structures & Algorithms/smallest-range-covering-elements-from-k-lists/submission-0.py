from heapq import heapify, heappop, heappush


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapify(heap)

        current_max = max(row[0] for row in nums)
        best_left, best_right = heap[0][0], current_max

        while heap:
            current_min, row, col = heappop(heap)

            if (
                current_max - current_min < best_right - best_left
                or (
                    current_max - current_min == best_right - best_left
                    and current_min < best_left
                )
            ):
                best_left, best_right = current_min, current_max

            if col + 1 == len(nums[row]):
                break

            next_value = nums[row][col + 1]
            current_max = max(current_max, next_value)
            heappush(heap, (next_value, row, col + 1))

        return [best_left, best_right]