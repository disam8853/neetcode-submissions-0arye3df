class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        ans = 0
        for p in prices:
            ans = max(ans, p - lowest)
            lowest = min(lowest, p)
        return ans