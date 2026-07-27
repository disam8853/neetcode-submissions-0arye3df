class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i,j] = dp[i-1, j-n] + dp[i-1, j+n]
        dp = collections.defaultdict(int)
        dp[0,0] = 1
        curMin = curMax = 0
        for i, n in enumerate(nums):
            curMax += abs(n)
            curMin -= abs(n)
            for j in range(curMin, curMax + 1):
                dp[i+1,j] = dp[i,j-n] + dp[i,j+n]
        return dp[len(nums),target]