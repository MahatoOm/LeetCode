class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        
        max_greater = 0
        
        max_decreasing = 0
        i = 0
        while i < len(nums)-1:
            count = 0
            count2 = 0
            while i < len(nums)-1 and nums[i] > nums[i+1]:
                count +=1
                i+=1 
            max_greater = max(max_greater, count)

            while i < len(nums)-1 and nums[i] < nums[i+1]:
                count2 +=1
                i+=1
            max_decreasing = max(max_decreasing, count2)

            if  i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
        return max(max_greater, max_decreasing) + 1 


        


        