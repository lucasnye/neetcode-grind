class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # before curr interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            # after curr interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # overlap
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        
        return res