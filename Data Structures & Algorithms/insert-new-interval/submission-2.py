class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            # newInterval.end < start
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            # newInterval.start > end
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        result.append(newInterval)

        return result