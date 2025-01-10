class Solution:
    def mySqrt(self, x: int) -> int:
        
        
        left = 0 
        right = x
        
        store = []
        while left <= right:
            
            mid = (left + right) // 2
            
            if mid * mid == x:
                
                return mid
                
            elif mid * mid >x:
                 right = mid -1
                    
            else: 
                store.append(mid)
                left = mid+1
                
        return store[-1] if store else 0
            
            
            
    