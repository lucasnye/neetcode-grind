class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])

        prev_end = intervals[0][1]
        count = 0

        for start, end in intervals[1:]:
            if start < prev_end:
                count += 1
                continue
            prev_end = end
        
        return count