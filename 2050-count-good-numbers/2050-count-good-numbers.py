class Solution:
    def countGoodNumbers(self, n: int) -> int:
   
        
        mod = 10**9 + 7

        # use fast exponentiation to calculate x^y % mod
        def quickmul(x: int, y: int) -> int:
            ret, mul = 1, x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                y //= 2
            return ret

        return quickmul(5, (n + 1) // 2) * quickmul(4, n // 2) % mod


#solution 1
        # total_sum = 1
        # # for i in range(n):

        # #     if i % 2 == 0:
        # #         total_sum *= 5 
        # #     elif i % 2 == 1:
        # #         total_sum *= 4


#solution 2
        # if n % 2 == 0:
        #     total_sum *= 5  **((n//2))
        #     total_sum *= 4 ** (n//2)
        # elif n % 2 == 1:
        #     total_sum *= 5 ** ((n//2) + 1) 
        #     total_sum *= 4 ** (n//2)

        # return total_sum % MOD