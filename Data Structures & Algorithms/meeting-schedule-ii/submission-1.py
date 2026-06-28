"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        hq = []
        ans = 0
        for interval in intervals:
            while hq and hq[0] <= interval.start:
                heapq.heappop(hq)
            heapq.heappush(hq, interval.end)
            ans = max(ans, len(hq))
        return ans