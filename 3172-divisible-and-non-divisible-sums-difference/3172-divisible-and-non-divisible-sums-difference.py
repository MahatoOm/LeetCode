class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        

        l = 1
        res = 0
        while l <= n:
            if l%m :
                res += l
            else:
                res -= l
            l += 1
            if l  > n:
                break
            if n%m :
                res += n
            else:
                res -= n
            n -= 1

        return res