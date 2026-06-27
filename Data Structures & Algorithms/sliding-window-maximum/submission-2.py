class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ary = deque()
        l = 0
        ans = []
        for r in range(len(nums)):
            n = nums[r]
            while ary and nums[ary[-1]] < n:
                ary.pop()
            ary.append(r)
            while ary and ary[0] < r - k + 1:
                ary.popleft()
            if r - l + 1 >= k:
                ans.append(nums[ary[0]])
        return ans