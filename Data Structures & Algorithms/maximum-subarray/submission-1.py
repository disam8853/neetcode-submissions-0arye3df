class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        curSum = 0
        ans = float('-inf')
        for n in nums:
            curSum += n
            if curSum < 0:
                curSum = 0
            ans = max(ans, curSum)
        return ans