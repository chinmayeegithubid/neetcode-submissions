from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meetings = sorted(intervals, key=lambda meeting: meeting.start)

        for i in range(1, len(meetings)):
            if meetings[i].start < meetings[i - 1].end:
                return False

        return True