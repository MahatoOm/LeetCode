class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) -1
        while left < right:
            
            mid = left + ( right - left) // 2
            
            #case1 
            if nums[mid] > nums[right]:
                left = mid + 1
            #case2
            elif nums[mid] < nums[right]:
                right = mid
            #case3
            else:
                right -=1 
                
        return nums[left]
    
    #not worked with 2 post processing    
#         while left +1 < right:
            
#             mid = (left + right) // 2
#             if nums[mid-1] > nums[mid] < nums[mid+1]:
#                 return nums[mid]
            
#             if nums[mid ] >= nums[mid-1] or nums[mid] <= nums[mid+1]:
#                 right = mid 
#             if nums[mid] < nums[mid-1] or nums[mid] > nums[mid+1]:
                
#                 left = mid
#             # if nums[mid] > nums[mid+1]:
#             #     left = mid
#             # if nums[mid] <= muns[mid+1]:
#             #     right = mid


#         if nums[left] < nums[right]:     
#             return nums[left]
#         elif nums[left] > nums[right]:     
#             return nums[right]
#         else:
#             return 0