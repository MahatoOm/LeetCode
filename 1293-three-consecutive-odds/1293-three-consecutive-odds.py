class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        for i in range(len(arr) -2):

            if arr[i] %2 == 0:
                continue
            if arr[i+1] % 2 == 0:
                i += 1
                continue
            if arr[i+2] % 2 == 0:
                i += 2
                continue
            return True
            


        return False