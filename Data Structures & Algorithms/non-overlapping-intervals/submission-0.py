class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        curStart, curEnd = intervals[0]
        out = 0
        for start, end in intervals[1:]:
            if curStart <= start < curEnd:
                curEnd = min(end, curEnd)
                out += 1
            else:
                curStart, curEnd = start, end
        return out