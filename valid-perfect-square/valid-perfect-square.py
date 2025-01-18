class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left = 1
        right = num
        
        '''
        Intution run a loop start from 1 to n
        and reduce area by halves each time 
        '''
        while left <= right :
            
            mid = (left + right) // 2
            
            if mid * mid == num:
                return True
            
            if mid * mid > num:
                right = mid -1
                
            else:
                left = mid + 1
                
        return False