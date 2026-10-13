from collections import deque


class Solution:
    def checkIfPrerequisite(self, numCourses: int,
                            prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ancestors = [set() for _ in range(numCourses)]

        for first, second in prerequisites:
            graph[first].append(second)
            indegree[second] += 1

        queue = deque(
            course for course in range(numCourses)
            if indegree[course] == 0
        )

        while queue:
            course = queue.popleft()

            for next_course in graph[course]:
                ancestors[next_course].add(course)
                ancestors[next_course].update(ancestors[course])

                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return [first in ancestors[second] for first, second in queries]