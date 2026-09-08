class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        curstart = intervals[0][0]
        curend = intervals[0][1]
        for start,end in intervals[1:]:
            if start <= curend:
                curend = max(end, curend)
            else:
                out.append([curstart, curend])
                curstart = start
                curend = end
        out.append([curstart, curend])
        return out