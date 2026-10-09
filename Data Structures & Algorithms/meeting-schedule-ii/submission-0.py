from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(meeting.start for meeting in intervals)
        ends = sorted(meeting.end for meeting in intervals)

        s = e = 0
        active = rooms = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                active += 1
                rooms = max(rooms, active)
                s += 1
            else:
                active -= 1
                e += 1

        return rooms