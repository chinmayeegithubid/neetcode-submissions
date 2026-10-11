class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            capacity = (left + right) // 2
            needed_days = 1
            load = 0

            for weight in weights:
                if load + weight > capacity:
                    needed_days += 1
                    load = 0
                load += weight

            if needed_days <= days:
                right = capacity
            else:
                left = capacity + 1

        return left