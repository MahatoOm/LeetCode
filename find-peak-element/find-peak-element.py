class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        # with binary template 2 where each iteration right is mid
#         l = 0
#         r = len(nums) -1
#         if r == 0:
#             return r
#         if r ==1:
#             return r if nums[r] > nums[0] else 0
        
#         while l < r:
            
#             m = (l+ r) //2
            
#             if nums[m-1]< nums[m] > nums[m+1]:
#                 return m
            
#             if  nums[m-1]< nums[m]< nums[m+1]:
#                 l = m + 1
#             else:
#                 r = m 
                
                
#         return r

        # with template 3 
        l = 0
        r = len(nums) -1
        if r == 0:
            return r
        if r ==1:
            return r if nums[r] > nums[0] else 0
        
        while l + 1 < r:
            
            m = (l+ r) //2
            
            if nums[m-1]< nums[m] > nums[m+1]:
                return m
            
            if  nums[m-1]< nums[m]< nums[m+1]:
                l = m 
            else:
                r = m 
                
                
        return l if nums[l] > nums[r] else r
            
                