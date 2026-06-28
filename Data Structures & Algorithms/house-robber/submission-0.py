class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, n in enumerate(nums):
            rob = n + (dp[i-2] if i > 1 else 0)
            noRob = dp[i-1] if i > 0 else 0
            dp[i] = max(rob, noRob)
        return dp[-1]