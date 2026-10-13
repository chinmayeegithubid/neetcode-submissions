class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]

        for preference in students:
            counts[preference] += 1

        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                return counts[0] + counts[1]

            counts[sandwich] -= 1

        return 0