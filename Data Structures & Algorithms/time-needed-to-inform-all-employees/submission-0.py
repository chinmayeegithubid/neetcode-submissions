class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        reports = [[] for _ in range(n)]

        for employee, boss in enumerate(manager):
            if boss != -1:
                reports[boss].append(employee)

        stack = [(headID, 0)]
        total_time = 0

        while stack:
            employee, received_at = stack.pop()
            total_time = max(total_time, received_at)

            for report in reports[employee]:
                stack.append(
                    (report, received_at + informTime[employee])
                )

        return total_time