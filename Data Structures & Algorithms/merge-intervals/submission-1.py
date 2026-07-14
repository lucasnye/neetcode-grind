class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x : x[0])

        prev = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            # check overlap between ith and (i-1)th interval
            if prev[0] <= intervals[i][1] and intervals[i][0] <= prev[1]:
                # merge
                prev = [min(prev[0], intervals[i][0]), max(prev[1], intervals[i][1])]
                continue
            else:
                res.append(prev)
                prev = intervals[i]
        
        res.append(prev)
        return res