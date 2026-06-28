class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        print(intervals)
        n = len(intervals)
        cnt = 0
        prevEnd = float('-inf')
        for start, end in intervals:
            if start < prevEnd:
                cnt += 1
            else:
                prevEnd = end
        return cnt