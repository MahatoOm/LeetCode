class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * n
        for i in  range(n):
            
            if i== 0:
                dp[i] =1
            elif i == 1:
                dp[i] = dp[i-1] *2
            elif i == 2:
                dp[i] = dp[i-1] * 2 + 1

            else:
                dp[i] = (2 * dp[i -1] + dp[i-3]) % MOD

        return dp[n-1]