class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        prev1 = prev2 = 0
        for i, n in enumerate(nums):
            rob = n + prev2
            noRob = prev1
            prev2, prev1 = prev1, max(rob, noRob)
        return prev1