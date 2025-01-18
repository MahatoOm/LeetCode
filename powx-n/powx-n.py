class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
            
        if n < 0:
            x = 1/x
            n = -n
        #because anything multiupleis with 1 result same value
        carry = 1
     # to track and update value of carry
        
        # we terminate the loop before n <=1

        while n > 1:
            # if even square the base and halves the power
            if n % 2 == 0:

                x = x * x
                n = n / 2
            else:
            # if odd square the base and halves the power and update the carry * base
            
                carry = carry * x

                x = x * x
                n = n // 2
        
        
        return x * carry