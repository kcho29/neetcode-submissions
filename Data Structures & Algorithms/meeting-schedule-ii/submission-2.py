"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
             return 0
        intervals.sort(key=lambda x: x.start)
        res, cur, priq = 1, 1, [intervals[0].end]
        heapq.heapify(priq)
        for inter in intervals[1:]:
            if inter.start < priq[0]: # add this meeting to our stack
                cur += 1
                heapq.heappush(priq, inter.end)
                res = max(res, cur)
            else:
                while priq and priq[0] <= inter.start:
                    heapq.heappop(priq)
                    cur -= 1
                heapq.heappush(priq, inter.end)
                cur += 1
        return res