class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        dp[i] = dp[i-1] + dp[i-2] if two digit <= 26
        '''
        if s and s[0] == '0': return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            c = int(s[i-1])
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i > 1 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]