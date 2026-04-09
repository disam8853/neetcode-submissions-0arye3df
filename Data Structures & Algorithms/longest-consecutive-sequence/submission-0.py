class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        res = 0
        for n in nums:
            if n in mp:
                continue
            maxN = minN = n
            mp[n] = [n, n]
            if n + 1 in mp:
                maxN = mp[n+1][1]
            if n - 1 in mp:
                minN = mp[n-1][0]
            mp[maxN][0] = minN
            mp[minN][1] = maxN
            res = max(res, maxN - minN + 1)
        return res