class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        n = len(intervals)
        i = 1
        while i < n:
            start, end = intervals[i]
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else :
                ans.append([start, end])
            i += 1
        return ans
            