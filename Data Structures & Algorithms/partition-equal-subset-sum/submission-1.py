class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for i in range(target, n-1, -1):
                if dp[i - n]:
                    dp[i] = True
                    # break
        return dp[target]