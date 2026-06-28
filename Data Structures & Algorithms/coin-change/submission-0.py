class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        coins = [1,5,10], amount = 12
        dp[12] = min(dp[2] + 1, dp[7] + 1, dp[2] + 2, )
        '''
        coins.sort()
        dp = collections.defaultdict(lambda: float('inf'))
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c > i:
                    break
                maxCnt = i // c
                for coinCnt in range(1, maxCnt+1):
                    dp[i] = min(dp[i], dp[i - c * coinCnt] + coinCnt)
        print(dp)
        return dp[amount] if dp[amount] < float('inf') else -1