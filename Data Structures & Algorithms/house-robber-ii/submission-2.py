class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(ary):
            if not ary:
                return 0
            dp = [0] * len(ary)
            for i, n in enumerate(ary):
                rob = n + (dp[i-2] if i > 1 else 0)
                noRob = dp[i-1] if i > 0 else 0
                dp[i] = max(rob, noRob)
            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))
