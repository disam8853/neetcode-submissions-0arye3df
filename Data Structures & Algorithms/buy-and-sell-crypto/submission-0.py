class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = j = 0
        ans = 0
        while j < len(prices):
            profit = prices[j] - prices[i]
            ans = max(ans, profit)
            while prices[j] - prices[i] < 0:
                i += 1
            j += 1

        return ans