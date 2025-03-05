class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        
        i = 1
        val = 0
        sum_val = 0
        while i < n:
            val = 2 *( 2 * (i) - 1) 
            sum_val += val

            i+=1


        return sum_val + 2 * (n) - 1