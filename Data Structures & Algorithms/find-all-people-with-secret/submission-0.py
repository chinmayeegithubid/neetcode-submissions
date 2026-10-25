from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(
        self,
        n: int,
        meetings: List[List[int]],
        firstPerson: int
    ) -> List[int]:

        meetings.sort(key=lambda meeting: meeting[2])

        knows = [False] * n
        knows[0] = knows[firstPerson] = True

        i = 0
        m = len(meetings)

        while i < m:
            time = meetings[i][2]
            graph = defaultdict(list)

            # Build the graph for this timestamp only.
            while i < m and meetings[i][2] == time:
                a, b, _ = meetings[i]
                graph[a].append(b)
                graph[b].append(a)
                i += 1

            # Start from participants who already know.
            queue = deque(person for person in graph if knows[person])

            while queue:
                person = queue.popleft()

                for neighbor in graph[person]:
                    if not knows[neighbor]:
                        knows[neighbor] = True
                        queue.append(neighbor)

        return [person for person in range(n) if knows[person]]