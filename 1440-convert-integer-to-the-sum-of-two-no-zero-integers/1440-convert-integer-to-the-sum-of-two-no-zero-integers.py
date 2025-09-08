class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        for i in range(1,n+1 //2 ):
            if "0" in str(i) or "0" in str(n-i):
                continue
            else:
                return i, n-i


        