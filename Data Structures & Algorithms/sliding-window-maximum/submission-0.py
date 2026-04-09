class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        ans = []
        idxMp = {}
        maxNum = -1
        hq = []
        while r < len(nums):
            n = nums[r]
            idxMp[n] = r
            heapq.heappush(hq, -n)
            if r - l + 1 > k:
                if idxMp[nums[l]] == l:
                    del idxMp[nums[l]]
                l += 1
            while -hq[0] not in idxMp:
                heapq.heappop(hq)
            if r - l + 1 == k:
                ans.append(-hq[0])
            r += 1

        return ans