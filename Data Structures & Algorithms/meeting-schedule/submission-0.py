"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        prevend = intervals[0].end
        for val in intervals[1:]:
            start, end = val.start, val.end
            if start < prevend:
                return False
            prevend = val.end
        return True

