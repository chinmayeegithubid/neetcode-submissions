from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        found_x = found_y = found_z = False

        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue

            found_x = found_x or a == x
            found_y = found_y or b == y
            found_z = found_z or c == z

            if found_x and found_y and found_z:
                return True

        return False