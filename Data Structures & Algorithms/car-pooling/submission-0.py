class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [0] * 1001

        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers

        onboard = 0

        for change in changes:
            onboard += change
            if onboard > capacity:
                return False

        return True