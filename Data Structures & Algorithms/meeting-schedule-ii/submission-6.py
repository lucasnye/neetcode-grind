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
        intervals.sort(key=lambda x : x.start)
        heap = []
        count = 0

        for interval in intervals:
            while heap and interval.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            count = max(count, len(heap))
        
        return count